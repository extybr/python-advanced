import sqlite3

with sqlite3.connect('hw_4_database.db') as connect:
    cursor = connect.cursor()

    sql = ['SELECT COUNT(*) FROM salaries WHERE salary < 5000',
           'SELECT AVG(salary) FROM salaries']

    row = [cursor.execute(i).fetchall() for i in sql]
    print(f'За чертой бедности, то есть получает меньше 5000 гульденов в год '
          f'находится: {row[0][0][0]} человек')

    average = round(row[1][0][0], 2)
    print('Средняя зарплата по острову N:', average)

    sql = ['SELECT COUNT(*) FROM salaries',
           'SELECT salary FROM salaries ORDER BY salary ASC']

    count = cursor.execute(sql[0]).fetchall()
    half = count[0][0] // 2
    index = half if half == 0 else half + 1
    summ_sorted = cursor.execute(sql[1]).fetchall()
    median = summ_sorted[index][0]
    print('Медианная зарплата:', median)

    total = count[0][0]
    sql = [f'SELECT salary FROM salaries ORDER BY salary DESC LIMIT 0.1 * {total}',
           f'SELECT salary FROM salaries ORDER BY salary ASC LIMIT 0.9 * {total}']

    rich, poor  = [cursor.execute(i).fetchall() for i in sql]
    coefficient = 100 * round(sum(i[0] for i in rich) / sum(i[0] for i in poor), 2)
    print(f'Число социального неравенства в процентах: {coefficient}%')
