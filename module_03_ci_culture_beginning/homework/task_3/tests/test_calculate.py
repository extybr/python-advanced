import unittest
from datetime import datetime
from module_03_ci_culture_beginning.homework.task_3.hw_3_2 import app


class TestCalculate(unittest.TestCase):
    """ Тест передачи и получения трат за год и месяц, тест калькуляции """
    def setUp(self):
        """ Инициализация. Функция запускается перед каждым тестом """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.get_url = '/calculate/'
        self.set_url = '/add/'
        self.storage = {'20221225': 300,
                        '20221226': 850}

    def test_length_type_correct(self):
        """ Проверка типов параметров """
        with self.assertRaises(TypeError):
            for key, value in self.storage.items():
                self.assertTrue(len(key) == 8)
                self.assertTrue(key == datetime.now().strftime("%Y%m%d"))
                self.assertTrue(self.storage[key], self.storage.values())
                if isinstance(key, str) and isinstance(value, int):
                    raise TypeError

    def test_can_set_and_get_correct(self):
        for key in self.storage.keys():
            response_set = self.app.get(self.set_url + key + '/' + str(self.storage[key]))
            response_text = response_set.data.decode()
            self.assertTrue(key in response_text)
            response_get = self.app.get(self.get_url + key)
            response_text = response_get.data.decode()
            self.assertTrue(key in response_text)
