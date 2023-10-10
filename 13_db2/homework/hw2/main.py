import sqlite3
import csv


def delete_wrong_fees(_cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    data = []
    with open(wrong_fees_file, 'r', encoding='cp1251') as fees:
        [data.append(timestamp_number) for timestamp_number in csv.reader(fees)]

    sql = "DELETE FROM table_fees WHERE truck_number = ? and timestamp = ?"
    [_cursor.execute(sql, numbers) for numbers in data[1:]]
    # result = _cursor.execute("SELECT COUNT(*) FROM table_fees")
    # print(result.fetchone()[0])


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as connect:
        cursor: sqlite3.Cursor = connect.cursor()
        delete_wrong_fees(cursor, "../wrong_fees.csv")
        connect.commit()
