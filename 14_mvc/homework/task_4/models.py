import sqlite3
from typing import Any, Optional, List

DATA: List[dict] = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.',
     'views_counter': 0},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville',
     'views_counter': 0},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy',
     'views_counter': 0}
]


class Book:

    def __init__(self, id: int, title: str, author: str, views_counter: int) -> None:
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.views_counter: int = views_counter

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)


def init_db(initial_records: List[dict]) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='table_books'; 
            """
        )
        exists: Optional[tuple[str,]] = cursor.fetchone()
        # now in `exist` we have tuple with table name if table really exists in DB
        if not exists:
            cursor.executescript(
                """
                CREATE TABLE `table_books` (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT, 
                    author TEXT,
                    views_counter INTEGER DEFAULT 0
                )
                """
            )
            cursor.executemany(
                """
                INSERT INTO `table_books`
                (title, author, views_counter) VALUES (?, ?, ?)
                """,
                [
                    (item['title'], item['author'], item['views_counter'])
                    for item in initial_records
                ]
            )


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()

        cursor.execute("UPDATE `table_books` "
                       "SET views_counter = views_counter + 1")

        cursor.execute("SELECT * from `table_books`")

        return [Book(*row) for row in cursor.fetchall()]


def insert_db(data: dict) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO `table_books`
            (title, author) VALUES (?, ?)
                """,
                (data['book_title'], data['author_name'])
        )


def get_books_by_author(author: str) -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()

        books_by_author = cursor.execute("SELECT * from `table_books` "
                                         "WHERE author = ?", (author,)).fetchall()

        cursor.execute("UPDATE `table_books` "
                       "SET views_counter = views_counter + 1 "
                       "WHERE author = ?", (author,))

        return [Book(*row) for row in books_by_author]


def get_the_most_popular_book() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()

        popular = cursor.execute("SELECT * from `table_books` "
                                 "ORDER BY views_counter DESC LIMIT 1").fetchall()

        cursor.execute("UPDATE `table_books` "
                       "SET views_counter = views_counter + 1 "
                       "WHERE id = ?", (popular[0][0],))

        return [Book(*row) for row in popular]
