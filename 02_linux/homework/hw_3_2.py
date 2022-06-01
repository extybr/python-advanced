"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int) -> str:
    global storage
    storage[date] = number
    return f"Добавлено {date}: {number} рублей"


@app.route("/calculate/<int:year>")
def calculate_year(year: int) -> str:
    global storage
    storage[str(year)] = 0
    summa = [int(value) for key, value in storage.items() if key.startswith(
             str(year)) and len(key) == 8]
    storage[str(year)] = sum(summa)
    return f"Траты за {year} год: {storage[str(year)]} рублей"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int) -> str:
    year_month = "{}{}".format(year, month) if month > 9 else "{}0{}".format(year, month)
    storage[year_month] = 0
    summa = [int(value) for key, value in storage.items() if key.startswith(year_month)]
    storage[year_month] = sum(summa)
    return f"Траты за {year} год {month} месяц: {storage[year_month]} рублей"


if __name__ == "__main__":
    app.run(debug=True)
