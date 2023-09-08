import sqlite3
from pathlib import Path


class DB:
    def __init__(self):
        self.db = "starwars.db"
        self.command_create = ('CREATE TABLE people '
                               '(name text, gender text, birth_year text)')
        self.command_insert = ("INSERT INTO people (name, gender, birth_year) "
                               "VALUES (?, ?, ?)")

    def db_command(self, cmd: str, data) -> None:
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        with connect:
            if not data:
                cursor.execute(cmd)
            else:
                cursor.execute(cmd, data)

    def insert_into_db(self, data) -> None:
        if not Path(self.db).exists():
            self.db_command(cmd=self.command_create, data='')
        self.db_command(cmd=self.command_insert, data=data)


db = DB()
