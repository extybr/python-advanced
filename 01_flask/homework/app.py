import datetime
from random import choice
from flask import Flask

app = Flask(__name__)
count = 0


@app.route('/hello_world')
def test_function():
    return 'Привет, мир!'


@app.route('/cars')
def cars_function():
    return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def cats_function():
    cats = ['Корниш рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мэйн-Кун', 'Манчкин']
    return choice(cats)


@app.route('/get_time/now')
def get_time_now_function():
    current_time = datetime.datetime.now()
    return f"Точное время {current_time}"


@app.route('/get_time/future')
def get_time_future_function():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"


@app.route('/get_random_word')
def get_random_word_function():
    with open('war_and_peace.txt', mode='r', encoding='utf-8') as file:
        words = file.read().split()
        word = choice(words)
        while len(word) < 3 or not word.isalpha():
            word = choice(words)
        return word


@app.route('/counter')
def counter_function():
    global count
    count += 1
    return f"Страница была открыта {count} раз"
