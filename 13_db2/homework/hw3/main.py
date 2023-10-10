import datetime
import sqlite3


def log_bird(_cursor: sqlite3.Cursor, bird_name: str, date_time: str) -> None:
    sql_create = """
    CREATE TABLE IF NOT EXISTS `table_bird`
    (id INTEGER PRIMARY KEY, 
    bird TEXT NOT NULL, 
    date TEXT NOT NULL);
    """
    _cursor.executescript(sql_create)
    sql_insert = "INSERT INTO `table_bird` (bird, date) VALUES (?, ?)"
    _cursor.execute(sql_insert, (bird_name, date_time))


def check_if_such_bird_already_seen(_cursor: sqlite3.Cursor, bird_name: str) -> bool:
    sql = "SELECT COUNT(*) FROM `table_bird` WHERE bird = ?"
    count_bird_name = _cursor.execute(sql, (bird_name,)).fetchone()
    return True if count_bird_name[0] > 1 else False


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name: str = input("Пожалуйста введите имя птицы\n> ")
    count_str: str = input("Сколько птиц вы увидели?\n> ")
    count: int = int(count_str)
    right_now: str = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("../homework.db") as connection:
        cursor: sqlite3.Cursor = connection.cursor()
        log_bird(cursor, name, right_now)

        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
