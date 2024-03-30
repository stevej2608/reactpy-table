from examples.books.db2 import BookDatabase
from utils import DT, log


def test_db():
    db = BookDatabase('sqlite:///books.db')
    assert db

    book_count = db.get_total_records()
    assert book_count == 100000

    dt = DT()

    books = db.search_books('Nice')

    log.info()


    assert len(books) == 379

   
