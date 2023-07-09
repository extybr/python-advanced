"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""

import json
import shlex
import subprocess
from typing import Dict


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    level = {}
    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            json_line = dict(json.loads(line))
            if not level.get(json_line['level'], {}):
                level[json_line['level']] = 1
            else:
                level[json_line['level']] += 1
    return level


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    time = {}
    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            json_line = dict(json.loads(line))
            if not time.get(json_line['time'][:2], {}):
                time[json_line['time'][:2]] = 1
            else:
                time[json_line['time'][:2]] += 1

    # вариант 1
    # for key, value in time.items():
    #     if value == max(time.values()):
    #         return int(key)

    # вариант 2
    # from collections import Counter
    # count_time = Counter(time).most_common()
    # return int(count_time[0][0])

    # вариант 3
    # from heapq import nlargest
    # count_time = nlargest(1, time, key=time.get)
    # return int(count_time[0])

    # вариант 4
    count_time = int(sorted(time, key=time.get)[-1])
    return count_time

def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    pattern = '"time": "05:[0-2]0:..", "level": "CRITICAL"'
    cmd = f"grep -c '{pattern}' skillbox_json_messages.log"
    args = shlex.split(cmd)
    output = subprocess.run(args, capture_output=True)
    result = int(output.stdout.decode())
    return result


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    pattern = 'dog'
    cmd = f"grep -c '{pattern}' skillbox_json_messages.log"
    args = shlex.split(cmd)
    output = subprocess.run(args, capture_output=True)
    result = int(output.stdout.decode())
    return result


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    from collections import Counter

    messages = []
    with open('skillbox_json_messages.log', 'r', encoding='utf-8') as file:
        for line in file:
            json_line = dict(json.loads(line))
            if json_line['level'] == 'WARNING':
                messages.extend(json_line['message'].encode().split())

    # вариант 1
    # result = {i: messages.count(i) for i in messages}
    # word = max(result, key=result.get).decode()

    # вариант 2
    count_word = Counter(messages)
    word = count_word.most_common(1)[0][0].decode()
    return word


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
