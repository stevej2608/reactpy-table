from datetime import datetime as dt
from typing import Optional, List

import sqlalchemy as db
from faker import Faker
from sqlmodel import Field, Session, SQLModel, col, select  # type:ignore

from reactpy_table import ColumnDef, Columns

COLS: Columns = [
    ColumnDef(name='id', label='#'),
    ColumnDef(name='title', label='Title'),
    ColumnDef(name='author', label='Author'),
    ColumnDef(name='publication_date', label='Date'),
    ColumnDef(name='genre', label='Genre'),
    ColumnDef(name='rating', label='Rating'),
    ]

engine = db.create_engine('sqlite:///books.db')

# https://sqlmodel.tiangolo.com/

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publication_date: dt
    genre: str
    rating: int

SQLModel.metadata.create_all(engine)

def generate_fake_books(num_records:int):
    fake = Faker()
    with Session(engine) as session:
        for _ in range(num_records):
            book = Book(
                title=fake.sentence(nb_words=4),
                author=fake.name(),
                publication_date=fake.date_between(start_date='-50y', end_date='today'),
                genre=fake.word(ext_word_list=['Fiction', 'Non-fiction', 'Mystery', 'Science Fiction', 'Romance']),
                rating=fake.pyint(min_value=1, max_value=5)
            )
            session.add(book)
        session.commit()


def search_books(title:str):
    with Session(engine) as session:
        statement = select(Book).where(Book.title == title)
        books = session.exec(statement).all()
    return books


# Function to filter books by genre
def filter_books_by_genre(genre:str):
    with Session(engine) as session:
        statement = select(Book).where(Book.genre == genre)
        books = session.exec(statement).all()
    return books

# https://sqlmodel.tiangolo.com/tutorial/fastapi/limit-and-offset

def get_paginated_books(page:int, per_page:int):
    offset = page * per_page
    with Session(engine) as session:
        heroes = session.exec(select(Book).offset(offset).limit(per_page)).all()
        return heroes


def create_book(title:str, author:str, publication_date: dt, genre: str, rating:int):
    with Session(engine) as session:
        book = Book(title=title, author=author, publication_date=publication_date, genre=genre, rating=rating)
        session.add(book)
        session.commit()


def update_book(book_id:int, title:str, author:str, publication_date: dt, genre:str, rating:int):
    with Session(engine) as session:
        statement = select(Book).where(col(Book.id) == book_id) # type: ignore
        book = session.exec(statement).one()
        if book:
            book.title = title
            book.author = author
            book.publication_date = publication_date
            book.genre = genre
            book.rating = rating
            session.commit()


def all_books() -> List[Book]:
    with Session(engine) as session:
        statement = select(Book)
        books = session.exec(statement).all()
        return list(books)



def delete_book(book_id:int):
    with Session(engine) as session:
        statement = select(Book).where(col(Book.id) == book_id)
        book = session.exec(statement).one()
        session.delete(book)
        session.commit()


# python -m examples.books.db

if __name__ == "__main__":
    generate_fake_books(100000)
