import unittest
from module_03_ci_culture_beginning.homework.task_4.person import Person, person


class TestPerson(unittest.TestCase):
    """ Тестирование класса Person """
    def setUp(self) -> None:
        """ Инициализация. Функция запускается перед каждым тестом """
        self.age = Person.get_age(person)
        self.name = Person.get_name(person)
        self.address = Person.get_address(person)
        self.homeless = Person.is_homeless(person)

    def test_parameters(self):
        """ Тест передаваемых параметров """
        self.assertTrue(self.age > 0)
        self.assertTrue(len(self.name) > 1)
        self.assertTrue(self.homeless in (0, 1))

    def test_type(self):
        """ Тест типов параметров """
        with self.assertRaises(TypeError):
            if isinstance(self.age, int) and isinstance(self.name, str) and isinstance(
                    self.homeless, bool) and (
                    self.address is None or isinstance(self.address, str)):
                raise TypeError
        with self.assertRaises(ValueError):
            if self.age > 0:
                raise ValueError
