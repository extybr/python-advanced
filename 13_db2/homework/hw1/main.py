import sqlite3


def check_if_vaccine_has_spoiled(
        _cursor: sqlite3.Cursor,
        _truck_number: str
) -> bool:
    sql = ("SELECT temperature_in_celsius "
           "FROM table_truck_with_vaccine "
           "WHERE truck_number = ? "
           "and temperature_in_celsius NOT BETWEEN 16 and 20")
    result = _cursor.execute(sql, (_truck_number,))

    if not _cursor.execute(sql[:-49], (_truck_number,)).fetchone():
        print('Грузовика с таким номером нет')

    return bool(result.fetchone())


if __name__ == '__main__':
    truck_number: str = input('Введите номер грузовика: ')
    with sqlite3.connect('../homework.db') as connect:
        cursor: sqlite3.Cursor = connect.cursor()
        spoiled: bool = check_if_vaccine_has_spoiled(cursor, truck_number)
        print('Испортилась' if spoiled else 'Не испортилась')
        connect.commit()
