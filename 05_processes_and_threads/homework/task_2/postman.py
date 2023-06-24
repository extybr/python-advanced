from remote_execution import app


def postman_post(_app):
    """ Отправка POST запроса. Аналог postman """
    _app.config["WTF_CSRF_ENABLED"] = False
    _app = _app.test_client()
    data = {"code": "print('Hello world! ' * 3)", "timeout": 3}
    base_url = '/run_code'
    response = _app.post(base_url, json=data)
    response_text = response.data.decode()
    print(response_text)

if __name__ == '__main__':
    postman_post(app)
