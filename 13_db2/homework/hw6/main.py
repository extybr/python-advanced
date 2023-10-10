import sqlite3
from calendar import weekday
from datetime import datetime, timedelta

start_year, start_month, start_day = 2020, 1, 1
end_year, end_month, end_day = 2020, 12, 31
schedule = dict()


def get_weekday() -> None:
    global schedule, start_year, start_month, start_day, end_year, end_month, end_day
    start_date = datetime(year=start_year, month=start_month, day=start_day)
    end_date = datetime(year=end_year, month=end_month, day=end_day)

    daily_sport = {'понедельник0': 'футбол', 'вторник1': 'хоккей',
                   'среда2': 'шахматы', 'четверг3': 'SUP сёрфинг',
                   'пятница4': 'бокс', 'суббота5': 'Dota2',
                   'воскресенье6': 'шах-бокс'}

    while start_date <= end_date:
        work_date = start_date.strftime("%Y-%m-%d")

        year, month, day = work_date.split('-')
        my = tuple(map(int, (year, month, day)))
        date = weekday(*my)
        for day, sport in daily_sport.items():
            if int(day[-1]) == date:
                schedule[work_date] = sport

        start_date += timedelta(days=1)


def employees(_cursor: sqlite3.Cursor, employee_id: int) -> str:
    sql = ("SELECT preferable_sport FROM table_friendship_employees "
           "WHERE id = ?")
    result, *_ = _cursor.execute(sql, (employee_id,)).fetchone()
    return result


def generate_schedule(_cursor: sqlite3.Cursor) -> None:
    global schedule, start_year, start_month, start_day, end_year, end_month, end_day
    start_date = datetime(year=start_year, month=start_month, day=start_day)
    end_date = datetime(year=end_year, month=end_month, day=end_day)
    number_of_people = 366
    start_person = 0
    while start_date <= end_date:
        work_date = start_date.strftime("%Y-%m-%d")
        people_to_add = []
        n = 0
        while n <= 10:
            person_idx = 1 + (start_person + n) % number_of_people
            if schedule[work_date] == employees(_cursor, person_idx):
                n += 1
                continue
            people_to_add.append((person_idx, work_date))
            n += 1
        _cursor.executemany("""
        INSERT INTO `table_friendship_schedule`(employee_id, date) 
        VALUES (?, ?);
        """, people_to_add,)
        start_date += timedelta(days=1)
        start_person += 1


def delete_table(_cursor: sqlite3.Cursor) -> None:
    sql_delete = "DELETE FROM table_friendship_schedule"
    _cursor.execute(sql_delete)


def check_work_schedule(_cursor: sqlite3.Cursor, employee_id: int) -> None:

    sql_1 = ('SELECT date '
             'FROM table_friendship_schedule t1 '
             'JOIN table_friendship_employees t2 ON t1.employee_id = t2.id '
             'and t1.employee_id = ?')
    result = _cursor.execute(sql_1, (employee_id,)).fetchall()
    [print(f'Дата выхода в смену: {day[0]}') for day in result]

    sql_2 = ('SELECT count(*) '
             'FROM table_friendship_schedule '
             'WHERE employee_id = ?')
    result, *_ = _cursor.execute(sql_2, (employee_id,)).fetchone()
    print(f'Сколько смен вышло за год: {result}')

    sql_3 = 'SELECT count(*) FROM table_friendship_schedule'
    result, *_ = _cursor.execute(sql_3).fetchone()
    print('Невозможно составить расписание равномерно') if result < 366 * 10 else ''


if __name__ == '__main__':
    with sqlite3.connect('../homework.db') as connect:
        cursor: sqlite3.Cursor = connect.cursor()
        get_weekday()
        # print(schedule)
        delete_table(cursor)
        generate_schedule(cursor)
        check_work_schedule(cursor, 10)
        connect.commit()
