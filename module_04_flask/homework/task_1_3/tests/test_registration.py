"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют
наборы данных, которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from module_04_flask.homework.task_1_3.hw1_registration import app


class TestValidation(unittest.TestCase):
    """ Тест корректности ввода данных пользователем """
    def setUp(self):
        """ Инициализация. Функция запускается перед каждым тестом """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration'
        self.data = {
                        "email": "test@example.com",
                        "phone": 99912345678,
                        "name": "John Connor",
                        "address": "New York",
                        "index": 187110,
                        "comment": "good boy"
                    }

    # def test_empty_key(self):
    #     """ Проверка значения на отсутствие """
    #     new = self.data.copy()
    #     for key in self.data:
    #         if key == 'comment':
    #             continue
    #         new[key] = ''
    #         response = self.app.post(self.base_url, json=new)
    #         response_text = response.data.decode()
    #         self.assertTrue(response_text.count('не должно быть пустым') == 1, msg='неверно')
    #         new[key] = self.data[key]

    def test_empty_email(self):
        """ Проверка значения на отсутствие """
        self.data['email'] = ''
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('не должно быть пустым') == 1)

    def test_invalid_email(self):
        """ Проверка значения на валидность """
        self.data['email'] = 'test@example.'
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('Invalid email address.') == 1)

    def test_empty_phone(self):
        """ Проверка значения на отсутствие """
        self.data['phone'] = int()
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('вы не ввели номер телефона') == 1)

    def test_invalid_phone(self):
        """ Проверка значения на валидность """
        self.data['phone'] = '999y1234567'
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('Not a valid integer value.') == 1)
        with self.assertRaises(TypeError):
            self.data['phone'] = 9991234567.1
            if isinstance(self.data['phone'], float):
                raise TypeError

    def test_range_phone(self):
        """ Проверка диапазона значения """
        self.data['phone'] = 99912345
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        print(response_text)
        self.assertTrue(response_text.count(
            'Число должно быть между 1000000000 and 99999999999.') == 1)

    def test_empty_name(self):
        """ Проверка значения на отсутствие """
        self.data['name'] = ''
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('не должно быть пустым') == 1)

    def test_empty_address(self):
        """ Проверка значения на отсутствие """
        self.data['address'] = ''
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('не должно быть пустым') == 1)

    def test_empty_index(self):
        """ Проверка значения на отсутствие """
        self.data['index'] = int()
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('не должно быть пустым') == 1)

    def test_invalid_index(self):
        """ Проверка значения на валидность """
        self.data['index'] = '187h535'
        response = self.app.post(self.base_url, json=self.data)
        response_text = response.data.decode()
        self.assertTrue(response_text.count('Not a valid integer value.') == 1)

    def test_ok_data(self):
        """ Проверка кода ответа """
        response = self.app.post(self.base_url, json=self.data)
        self.assertEqual(response.status, '200 OK')

    def test_bad_data(self):
        """ Проверка кода ответа с пустым телом POST """
        response = self.app.post(self.base_url, json={})
        self.assertEqual(response.status, '400 BAD REQUEST')


if __name__ == '__main__':
    unittest.main()
