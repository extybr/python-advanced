"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

from flask import Flask, request
from typing import List
import shlex
import subprocess

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    command = "ps"
    args: List[str] = request.args.getlist('arg')
    clean = [shlex.quote(i) for i in args]
    full_command = shlex.split(f"{command} {''.join(clean)}")
    result = subprocess.run(full_command, capture_output=True).stdout.decode()
    return "<h3><font color='blue'><pre>{result}</pre></font></h3>".format(result=result)


if __name__ == "__main__":
    app.run(debug=True)
