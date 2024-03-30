from typing import List, Optional
from sqlalchemy import inspect
from sqlalchemy import text
from sqlalchemy import create_engine, Column, Integer, String, Connection
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from utils import log, logging, DT

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

        # Check if the books table exists

        inspector = inspect(self.engine)
        if inspector.has_table('book'):

            # The books table exists, create the books_fts5 table if it doesn't exist

            with self.engine.connect() as connection:
                if not inspector.has_table('book_fts'):
                    # connection.execute(text(f"CREATE VIRTUAL TABLE {BookFTS.__tablename__} USING fts5(title, author, publication_date, genre, rating, tokenize='porter')"))
                    connection.execute(text(f"CREATE VIRTUAL TABLE {BookFTS.__tablename__} USING fts5(title, author, publication_date, genre, rating)"))
                    self._populate_fts_index(connection)
        else:
            # If the books table doesn't exist, create all tables
            Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)


    def _populate_fts_index(self, connection: Connection) -> None:
        log.info('Populating FTS table...')
        books: List[Book] = connection.execute(Book.__table__.select()).fetchall() # type: ignore

        for book in books:
            connection.execute(BookFTS.__table__.insert().values(
                        rowid=book.id,
                        title=book.title,
                        author=book.author,
                        publication_date=book.publication_date,
                        genre=book.genre,
                        rating=book.rating
                        ))

        connection.commit()


    def get_total_records(self) -> int:
        with self.Session() as session:
            rows = session.query(Book).count()
            return rows


    def create_book(self, book: Book) -> None:
        session = self.Session()
        session.add(book)
        session.commit()
        self._update_fts_index(session, book)
        session.close()

    def read_book(self, book_id: int) -> Optional[Book]:
        session = self.Session()
        book = session.query(Book).filter_by(id=book_id).first()
        session.close()
        return book

    def update_book(self, book: Book) -> None:
        session = self.Session()
        session.merge(book)
        session.commit()
        self._update_fts_index(session, book)
        session.close()

    def delete_book(self, book_id: int) -> None:
        session = self.Session()
        book = session.query(Book).filter_by(id=book_id).first()
        if book:
            session.delete(book)
            session.commit()
            self._delete_from_fts_index(session, book_id)
        session.close()

    def list_books(self) -> List[Book]:
        session = self.Session()
        books = session.query(Book).all()
        session.close()
        return books

    def search_books(self, query: str) -> List[Book]:
        session = self.Session()

        book_ids = session.execute(text(f"SELECT rowid FROM {BookFTS.__tablename__} WHERE {BookFTS.__tablename__} MATCH '{query}'"))

        book_ids = [book_id[0] for book_id in book_ids]
        books = session.query(Book).filter(Book.id.in_(book_ids)).all()
        session.close()
        return books

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

    books = db.search_books('Nice')
    print(f"Found {len(books)} books in {dt()} ms")

    books = db.search_books('Boy')
    print(f"Found {len(books)} books in {dt()} ms")

    books = db.search_books('Boy')
    print(f"Found {len(books)} books in {dt()} ms")
