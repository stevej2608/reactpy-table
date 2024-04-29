import logging
from datetime import datetime
from typing import Any, List, Optional, Sequence, Tuple, cast

from faker import Faker
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlmodel import Field, Session, SQLModel, col, select, text  # type:ignore

from reactpy_table import ColumnDef, Columns
from utils import DT

log = logging.getLogger(__name__)

COLS: Columns = [
    ColumnDef(name='id', label='#'),
    ColumnDef(name='title', label='Title'),
    ColumnDef(name='author', label='Author'),
    ColumnDef(name='publication_date', label='Date'),
    ColumnDef(name='genre', label='Genre'),
    ColumnDef(name='rating', label='Rating'),
    ]


class Book_FTS(SQLModel, table=True):
    rowid: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publication_date: datetime
    genre: str
    rating: int

    @classmethod
    def table_name(cls) -> str:
        return str(cls.__tablename__) # type:ignore


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publication_date: datetime
    genre: str
    rating: int

class BookDatabase:

    def __init__(self, url: str):
        self.engine = create_engine(url='sqlite:///books.db')

        # Create the FTS table using SQL statements

        inspector = inspect(self.engine)

        if not inspector.has_table(Book_FTS.table_name()):
            with self.engine.connect() as connection:
                connection.execute(text(f"CREATE VIRTUAL TABLE {Book_FTS.table_name()} USING fts5(title, author, publication_date, genre, rating)"))

        SQLModel.metadata.create_all(self.engine)

        # Create the books table if needed

        if self.get_row_count(Book) == 0:
            self._generate_fake_books(100000)

        # Populate the FTS table if it's empty

        if self.get_row_count(Book_FTS) == 0:
            self._populate_fts_index()

        # Keep the count of the records

        self.total_rows = self.get_row_count(Book)


    def _generate_fake_books(self,num_records:int):
        log.info('Populating Books table...')
        Faker.seed(4321)
        fake = Faker()
        with Session(self.engine) as session:
            while num_records > 0:
                recs = num_records if num_records < 10000 else 10000
                num_records -= recs
                session.bulk_insert_mappings(
                    Book,
                    [ dict(
                        title=fake.sentence(nb_words=4),
                        author=fake.name(),
                        publication_date=fake.date_between(start_date='-50y', end_date='today'),
                        genre=fake.word(ext_word_list=['Fiction', 'Non-fiction', 'Mystery', 'Science Fiction', 'Romance']),
                        rating=fake.pyint(min_value=1, max_value=5)
                    ) for _ in range(0, recs)]
                )
            session.commit()


    def _populate_fts_index(self) -> None:
        log.info('Populating FTS table...')
        books: List[Book] = self.list_books()
        with Session(self.engine) as session:
            num_records = len(books)
            skip = 0
            while num_records > 0:
                bulk_count = num_records if num_records < 10000 else 10000
                bulk_recs = books[skip: skip+bulk_count]
                session.bulk_insert_mappings(
                    Book_FTS,
                    [dict(
                        rowid=rec.id,
                        title=rec.title,
                        author=rec.author,
                        publication_date=rec.publication_date,
                        genre=rec.genre,
                        rating=rec.rating
                        ) for rec in bulk_recs]
                )
                skip += bulk_count
                num_records -= bulk_count

            session.commit()


    def get_row_count(self, table:SQLModel) -> int:
        with Session(self.engine) as session:
            # pylint: disable=not-callable
            statement = select(func.count()).select_from(table) # type: ignore
            result = session.exec(statement)
            count = result.one()
            return count


    def get_total_records(self) -> int:
        return self.get_row_count(Book)


    def create_book(self, book: Book) -> None:
        with Session(self.engine) as session:
            session.add(book)
            session.commit()
            self._update_fts_index(session, book)
            self.total_rows += 1


    def read_book(self, book_id: int) -> Optional[Book]:
        with Session(self.engine) as session:
            statement = select(Book).where(col(Book.id) == book_id) # type: ignore
            book = session.exec(statement).one()
            return book


    def update_book(self, book: Book) -> None:
        with Session(self.engine) as session:
            db_book = session.get(Book, book.id)
            if db_book:
                db_book.title = book.title
                db_book.author = book.author
                db_book.publication_date = book.publication_date
                db_book.genre = book.genre
                db_book.rating = book.rating
                session.commit()
            else:
                raise ValueError(f"Book with ID {book.id} not found.")


    def delete_book(self, book_id: int) -> None:
        with Session(self.engine) as session:
            db_book = session.get(Book, book_id)
            if db_book:
                session.delete(db_book)
                session.commit()
                self._delete_from_fts_index(session, book_id)
                self.total_rows -= 1


    def list_books(self) -> List[Book]:
        with Session(self.engine) as session:
            statement = select(Book)
            books = session.exec(statement).all()
            return list(books)


    def get_paginated_books(self, skip:int, limit:int, col_id:str='id', desc:str='ASC') -> Tuple[List[Book], int]:
        """Return a page of books together with the total number of books in the database

        Args:
            skip (int, optional): Skip n rows. Defaults to 0.
            limit (int, optional): Return n rows. Defaults to 20.
            col_id (str, optional): Sort returned rows on given column. Defaults to 'id'.
            desc (str, optional): Sort rows ASC or DESC. Defaults to 'ASC'.

        Returns:
            Tuple[List[Book], int]: Books and count of total books
        """

        with Session(self.engine) as session:

            column_ref: InstrumentedAttribute[Any] = Book.__dict__[col_id]
            order = column_ref.asc() if desc=='ASC' else column_ref.desc()

            stmt = select(Book).order_by(order).offset(skip).limit(limit)

            books = session.exec(stmt).all()
            return list(books), self.total_rows


    def get_books(self, query: str="", skip:int=0, limit:int=20, col_id:str='id', desc:str='ASC') -> Tuple[List[Book], int]:
        """Get filtered, sorted and paginated rows of books

        Args:
            query (str): Query string for full text search
            skip (int, optional): Skip n rows. Defaults to 0.
            limit (int, optional): Return n rows. Defaults to 20.
            col_id (str, optional): Sort returned rows on given column. Defaults to 'id'.
            desc (str, optional): Sort rows ASC or DESC. Defaults to 'ASC'.

        Returns:
            Tuple[List[Book], int]: Books and count of total matching rows
      
        """

        with Session(self.engine) as session:
            if query:

                try:
                    cursor = cast(Sequence[Book_FTS], session.exec(text(f"""
                                    SELECT rowid FROM {Book_FTS.table_name()} 
                                    WHERE {Book_FTS.table_name()} 
                                    MATCH '{query}'
                                    """))) # type: ignore
                except OperationalError:
                    return [], 0

                if cursor:


                    # Get query matching book ids
                    book_ids = [row.rowid for row in cursor]
                    total_count = len(book_ids)

                    # Column to sort on and sort direction
                    column_ref = getattr(Book, col_id)
                    order = column_ref.asc() if desc == 'ASC' else column_ref.desc()

                    # Get the books from the main table

                    # pylint: disable=no-member
                    stmt = select(Book).where(Book.id.in_(book_ids)).order_by(order).offset(skip).limit(limit) # type: ignore

                    books = list(session.exec(stmt).all())

                    return books, total_count
                else:
                    return [], 0
            else:
                return self.get_paginated_books(skip=skip, limit=limit, col_id=col_id, desc=desc)


    def _update_fts_index(self, session: Session, book: Book) -> None:
        with Session(self.engine) as session:
            db_book = session.get(Book_FTS, book.id)
            if db_book:
                db_book.title = book.title
                db_book.author = book.author
                db_book.publication_date = book.publication_date
                db_book.genre = book.genre
                db_book.rating = book.rating
                session.commit()
            else:
                raise ValueError(f"Book_FTS with ID {book.id} not found.")


    def _delete_from_fts_index(self, session: Session, book_id: int) -> None:
        with Session(self.engine) as session:
            db_book = session.get(Book_FTS, book_id)
            if db_book:
                session.delete(db_book)
                session.commit()
            else:
                raise ValueError(f"Book_FTS with ID {book_id} not found.")


if __name__ == "__main__":
    log.setLevel(logging.INFO)
    db = BookDatabase('sqlite:///books.db')

    dt = DT()

    books, count  = db.get_books(query='Nice')
    print(f"Found {len(books)}/{count} books in {dt()} ms")

    books, count  = db.get_books(query='Boy')
    print(f"Found {len(books)}/{count} books in {dt()} ms")

    books, count = db.get_books(query='Boy')
    print(f"Found {len(books)}/{count} books in {dt()} ms")

    books, page_count = db.get_paginated_books(200, 20)
    print(f"Paginate {len(books)} books (page 10 of 200), in {dt()} ms")
