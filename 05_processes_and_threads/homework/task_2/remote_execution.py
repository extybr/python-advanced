"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

import subprocess
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)

class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired('не должно быть пустым')])
    timeout = IntegerField(validators=[InputRequired('не должно быть пустым'),
                                       NumberRange(min=0, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int) -> str:
    # cmd = f'python -c "{code}"'
    cmd = f'prlimit --nproc=1:1 python -c "{code}"'
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(timeout=timeout)
        return "Результат: {}".format(outs.decode())
    except subprocess.TimeoutExpired:
        proc.kill()
        return "Исполнение кода не уложилось в данное время"


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        result = run_python_code_in_subproccess(code, timeout)
        return result
    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
