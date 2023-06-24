import unittest
from module_05_processes_and_threads.homework.task_2.remote_execution import app


class TestValidation(unittest.TestCase):
    """ Тест корректности ввода данных пользователем """
    def setUp(self):
        """ Инициализация. Функция запускается перед каждым тестом """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/run_code'
        self.data = {
                        "code": "print('Hello world!')",
                        "timeout": 0.9
                    }

    def test_empty_code(self):
        """ Проверка значения на отсутствие """
        self.data['code'] = ''
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('не должно быть пустым') == 1)

    def test_shell_code(self):
        """ Проверка небезопасного кода """
        self.data['code'] = "print('Hello world!'); shell=True"
        self.assertTrue(self.data['code'].count('shell=True') == 1)

    def test_empty_timeout(self):
        """ Проверка значения на отсутствие """
        self.data['timeout'] = int()
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('не должно быть пустым') == 1)

    def test_range_timeout(self):
        """ Проверка диапазона значения """
        self.data['timeout'] = 31
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count(
            'Number must be between 0 and 30.') == 1)

    def test_min_range_timeout(self):
        """ Проверка диапазона значения """
        self.data['timeout'] = 0.9
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count(
            'Исполнение кода не уложилось в данное время') == 1)


if __name__ == '__main__':
    unittest.main()
