from examples.books.db2 import BookDatabase


db = BookDatabase("sqlite:///books.db")

# pytest tests/test_db.py

def test_total_records():
    book_count = db.get_total_records()
    assert book_count == 100000

def test_pagination():
    books, page_count = db.get_paginated_books(2, 20)
    assert page_count == 5000
    assert len(books) == 20

def test_search():
    books = db.search_books("Nice")
    assert len(books) == 379
