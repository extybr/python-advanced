# from freezegun import freeze_time
from datetime import datetime
import unittest
from module_03_ci_culture_beginning.homework.task_1.hello_word_with_day import app


class TestDayUsername(unittest.TestCase):
    """ Тест корректности дня недели и имени пользователя """
    def setUp(self):
        """ Инициализация. Функция запускается перед каждым тестом """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_username_weekday(self):
        """ Тест получения дня недели и имени пользователя """
        username = 'username'
        weekday = {
            0: "Хорошего понедельника",
            1: "Хорошего вторника",
            2: "Хорошей среды",
            3: "Хорошего четверга",
            4: "Хорошей пятницы",
            5: "Хорошей суббота",
            6: "Хорошего воскресенья",
        }
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        day = datetime.today()
        self.assertTrue(username in response_text)
        self.assertTrue(str(type(day)) == "<class 'datetime.datetime'>")
        self.assertNotEqual(username, weekday[day.weekday()])


if __name__ == '__main__':
    unittest.main()
