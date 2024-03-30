from typing import Any, List, Optional, Tuple

from faker import Faker
from sqlalchemy import inspect, Column, Integer, String, create_engine, select, text, Table
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute

from utils import DT, log, logging

Base = declarative_base()

class BookFTS(Base):
    __tablename__ = 'book_fts'
    rowid = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(String)
    genre = Column(String)
    rating = Column(Integer)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(String)
    genre = Column(String)
    rating = Column(Integer)

class BookDatabase:

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)

        # Create the FTS table using SQL statements

        inspector = inspect(self.engine)

        if not inspector.has_table('book_fts'):
            with self.engine.connect() as connection:
                connection.execute(text(f"CREATE VIRTUAL TABLE {BookFTS.__tablename__} USING fts5(title, author, publication_date, genre, rating)"))

        Base.metadata.create_all(self.engine)

        # Create the books table if needed

        if self.get_row_count(Book) == 0:
                self._generate_fake_books(100000)

        self.session = sessionmaker(bind=self.engine)

        # Populate the FTS table if it's empty

        if self.get_row_count(BookFTS) == 0:
            self._populate_fts_index()

        # Keep the count of the records

        with Session(self.engine) as session:
            self.total_rows = session.query(Book).count() # type: ignore


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
                    BookFTS,
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


    def get_row_count(self, table:Table) -> int:
        with Session(self.engine) as session:
            rows = session.query(table).count()
            return rows


    def get_total_records(self) -> int:
        return self.get_row_count(Book)


    def create_book(self, book: Book) -> None:

        with self.session() as session:
            session.add(book)
            session.commit()

        self._update_fts_index(session, book)
        self.total_rows += 1


    def read_book(self, book_id: int) -> Optional[Book]:
        with self.session() as session:
            book = session.query(Book).filter_by(id=book_id).first()
            return book


    def update_book(self, book: Book) -> None:

        with self.session() as session:
            session.merge(book)
            session.commit()

        self._update_fts_index(session, book)
        session.close()


    def delete_book(self, book_id: int) -> None:
        with self.session() as session:
            book = session.query(Book).filter_by(id=book_id).first()
            if book:
                session.delete(book)
                session.commit()
                self._delete_from_fts_index(session, book_id)
                self.total_rows -= 1


    def list_books(self) -> List[Book]:
        with self.session() as session:
            books = session.query(Book).all()
            return books


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

            books = [row[0] for row in session.execute(stmt).all()]
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

        with self.session() as session:
            if query:

                # Get the book IDs that match the query from the FTS table

                cursor = session.execute(text(f"""
                                SELECT rowid FROM {BookFTS.__tablename__} 
                                WHERE {BookFTS.__tablename__} 
                                MATCH '{query}'
                                """))
                if cursor:

                    # Get query matching book ids

                    book_ids = [row[0] for row in cursor]
                    total_count = len(book_ids)

                    # Column to sort on and sort direction

                    column_ref: InstrumentedAttribute[Any] = Book.__dict__[col_id]
                    order = column_ref.asc() if desc=='ASC' else column_ref.desc()

                    # Get the books from the main table

                    stmt = select(Book).filter(Book.id.in_(book_ids)).order_by(order).offset(skip).limit(limit)
                    books = [row[0] for row in session.execute(stmt).all()]

                    return books, total_count
                else:
                    return [], 0
            else:
                return self.get_paginated_books(skip=skip, limit=limit, col_id=col_id, desc=desc)



    def _update_fts_index(self, session: Session, book: Book) -> None:
        session.execute(BookFTS.__table__.insert().values(
            rowid=book.id,
            title=book.title,
            author=book.author,
            publication_date=book.publication_date,
            genre=book.genre,
            rating=book.rating
            ))

    def _delete_from_fts_index(self, session: Session, book_id: int) -> None:
        session.execute(BookFTS.__table__.delete().where(BookFTS.rowid == book_id))


# python -m examples.books.db2

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
