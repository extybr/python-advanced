"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email                  # , NumberRange
from module_04_flask.homework.task_1_3.hw2_validators import NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired('не должно быть пустым'), Email()])
    # phone = IntegerField(validators=[InputRequired('не должно быть пустым'), NumberRange(
    #     min=1000000000, max=99999999999)])
    phone = IntegerField(validators=[InputRequired('вы не ввели номер телефона'),
                                     NumberLength(minimum=1000000000, maximum=99999999999,
                                                  message=None)])
    name = StringField(validators=[InputRequired('не должно быть пустым')])
    address = StringField(validators=[InputRequired('не должно быть пустым')])
    index = IntegerField(validators=[InputRequired('не должно быть пустым')])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()
    # import json
    # with open('registration.json', 'w', encoding='utf-8') as reg:
    #     reg.write(json.dumps(form.data, indent=4))
    if form.validate_on_submit():
        name, email, phone = form.name.data, form.email.data, form.phone.data
        return f"Successfully registered user {name} with email {email} and with phone +7{phone}"
    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
