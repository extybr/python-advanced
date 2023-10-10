import sqlite3
import httpx
from bs4 import BeautifulSoup
from random import randint
from typing import List


def get_club_names() -> List[tuple]:
    """ Парсим данные для последущей загрузки в базу данных """
    teams = []
    country = ''
    level = ['strong', 'average', 'average', 'weak']
    try:
        url = 'https://ru.uefa.com/nationalassociations/leaguesandcups/'
        response = httpx.get(url, timeout=5).text
        soup = BeautifulSoup(response, 'html.parser')
        items = soup.find_all('span', class_='standing-domestic-identifier-name')
        temp_level = level.copy()
        for count, team in enumerate(items, 1):
            team = team.text.strip()
            team_level = temp_level.pop()
            temp_level = temp_level if temp_level else level.copy()
            team_number: int = randint(1000, 9000)
            if count % 6 == 0:
                continue
            elif count % 6 == 1:
                country = team.split(' ')[0]
            else:
                teams.append((team_number, team, country, team_level))
    except Exception:
        pass
    # print(len(teams))  # 48
    return teams


def generate_test_data(_cursor: sqlite3.Cursor, _number_of_groups: int) -> None:
    teams: List[tuple] = get_club_names()

    sql = ("INSERT INTO uefa_commands (command_number, command_name, "
           "command_country, command_level) VALUES (?, ?, ?, ?)")
    _cursor.executemany(sql, teams[:_number_of_groups * 4])

    sql_insert = ("INSERT INTO uefa_draw (command_number, group_number) "
                  "VALUES (?, ?)")
    data = []
    group_number, divider = 1, 1
    for command_number in teams[:_number_of_groups * 4]:
        data.append((command_number[0], group_number))
        if divider % 4 == 0:
            group_number += 1
        divider += 1
    _cursor.executemany(sql_insert, data)


if __name__ == '__main__':
    number_of_groups: int = int(input('Введите количество групп (от 4 до 12): '))
    while number_of_groups < 4 or number_of_groups > 12:
        print('не выполнено условие')
        number_of_groups = int(input('Введите количество групп (от 4 до 12): '))
    # condition = 3 < number_of_groups < 13
    # number_of_groups = number_of_groups if condition else 8
    with sqlite3.connect('../homework.db') as connect:
        cursor: sqlite3.Cursor = connect.cursor()
        generate_test_data(cursor, number_of_groups)
        connect.commit()
