import sqlite3


def insert_into_db(data):
    sql = ("INSERT INTO table_car (car_number, name, description, belongs_to) "
           "VALUES (?, ?, ?, ?)")
    con = sqlite3.connect("hw_1_database.db")
    cursor = con.cursor()
    with con:
        try:
            cursor.executemany(sql, data)
        except sqlite3.DatabaseError as err:
            print("Ошибка:", err)
        else:
            print("Запрос успешно выполнен")
            con.commit()


def read_db(data):
    for i in data:
        name = i[-1].split(' ')[0]
        sql = f"SELECT passport_id FROM table_people WHERE name LIKE '%{name}%'"
        # print(sql)
        con = sqlite3.connect("hw_1_database.db")
        cursor = con.cursor()
        with con:
            try:
                result = cursor.execute(sql).fetchall()
                i[-1] = result[0][0]
                # i.extend(result[0])
            except sqlite3.DatabaseError as err:
                print("Ошибка:", err)
    return data


with open('README.md', 'r', encoding='utf-8') as readme:
    info = []
    sample = readme.readlines()[9:29]
    for line in sample:
       mass = line[8:-3].split('|')
       mass = [i.strip() for i in mass]
       info.append(mass)


new_info = read_db(info)
# print(new_info)
insert_into_db(new_info)

