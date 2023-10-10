import sqlite3


def ivan_sovin_the_most_effective(_cursor: sqlite3.Cursor, _name: str) -> None:
    if _name == "Иван Совин":
        print('Эффективного менеджера запрещено удалять и поощрять !!!')
        return

    const = 100000
    addition = 'а' if _name.split(' ')[0][-1] == 'а' else ''

    sql = f"SELECT * FROM table_effective_manager WHERE name LIKE '%{_name}%'"
    result = _cursor.execute(sql).fetchone()

    if result:
        salary = result[2]

        if not (salary := salary + salary * 0.1) > const:
            sql_update = (f"UPDATE table_effective_manager "
                          f"SET salary = {round(salary)} "
                          f"WHERE name LIKE '%{_name}%'")
            _cursor.execute(sql_update)
            print(f'Сотрудник {_name} получил{addition} повышение зарплаты')

        else:
            sql_delete = (f"DELETE FROM table_effective_manager "
                          f"WHERE name LIKE '%{_name}%'")
            _cursor.execute(sql_delete)
            print(f'Сотрудник {_name}, уволен{addition}')

    else:
        print('Ошибка, такого сотрудника нет в базе данных')


if __name__ == '__main__':
    name: str = input('Введите имя сотрудника: ')
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, name)
        conn.commit()
