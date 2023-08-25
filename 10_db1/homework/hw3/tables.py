import sqlite3

with sqlite3.connect('hw_3_database.db') as connect:
    cursor = connect.cursor()

    data = ['SELECT count(*) FROM table_1', 'SELECT count(*) FROM table_2',
            'SELECT count(*) FROM table_3']
    row = [cursor.execute(i).fetchone()[0] for i in data]
    print(' Количество записей '.center(50, '*'))
    print('в первой таблице:', row[0])
    print('во второй таблице:', row[1])
    print('в третьей таблице:', row[2])

    print(' В таблице table_1 уникальных записей '.center(50, '*'))
    data = ['SELECT count(DISTINCT id) FROM table_1', 'SELECT count(DISTINCT '
                                                      'value) FROM table_1']
    id_1, value_1 = [cursor.execute(i).fetchone()[0] for i in data]
    print('по <id>:', id_1)
    print('по <value>:', value_1)

    print(' Записей из таблицы table_1 встречается в table_2 '.center(55, '*'))
    data = ['SELECT COUNT(*) AS count_tables FROM table_1 t1 JOIN table_2 t2 '
            'ON t1.value = t2.value or t1.id = t2.id',
            'SELECT COUNT(*) AS count_tables FROM table_1 t1 JOIN table_2 t2 '
            'ON t1.value = t2.value']
    id_2,  value_2 = [cursor.execute(i).fetchall() for i in data]
    print('по <id> и <value>:', id_2[0][0])
    print('по <value>:', value_2[0][0])

    print(' Записей из таблицы table_1 встречается и в table_2, и в table_3 '
          ''.center(69, '*'))
    data = '''SELECT * FROM table_1 INTERSECT SELECT * FROM table_2 
    INTERSECT SELECT * FROM table_3'''
    id_value_3 = cursor.execute(data).fetchall()
    print('по <id> и <value>:', len(id_value_3))


