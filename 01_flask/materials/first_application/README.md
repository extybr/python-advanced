### Как запустить
* создайте и активируйте виртуальное окржение
* установите зависимости из файла requirements.txt
* выполните следующие команды:

* * для Linux/MacOS
    ```bash
    cd repo
    export FLASK_APP="app.py"
    export FLASK_DEBUG=1
    python -m flask run --port=5555
    ```
* *  для Windows:
        ```bash
        cd repo
        setx FLASK_APP "app.py"
        setx FLASK_DEBUG 1
        python -m flask run --port=5555
        ```
* go to http://127.0.0.0:5555/test
