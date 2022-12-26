import unittest
from module_03_ci_culture_beginning.homework.task_2.decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    """ Тест расшифровки """
    def setUp(self) -> None:
        """ Инициализация. Функция запускается перед каждым тестом """
        self.text = "абра-кадабра"

    def test_decrypt(self):
        """ Тест проверки правильности расшифровки """
        magic_1 = ["абра-кадабра.", "абраа..-кадабра", "абраа..-.кадабра", "абра--..кадабра",
                   "абрау...-кадабра"]
        magic_2 = ["абра........", "абр......a.", "1..2.3", ".", "1......................."]
        magic_3 = ["", "a", "23", "", ""]
        with self.subTest():
            [self.assertEqual(decrypt(i), self.text) for i in magic_1]
            [self.assertTrue(decrypt(i[0]) == i[1]) for i in zip(magic_2, magic_3)]
