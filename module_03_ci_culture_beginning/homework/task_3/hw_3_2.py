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
