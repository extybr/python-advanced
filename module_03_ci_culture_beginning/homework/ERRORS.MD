# Исправления ошибок класса Person
+ Импорт datetime из модуля datetime
  ```python
    from datetime import datetime
  ```
+ Конструктор. При передаче параметра address="" заменил на address=None
  ```python
    def __init__(self, name, year_of_birth, address=None):
        self.name = name
        self.yob = year_of_birth
        self.address = address
  ```
+ Метод get_age. Переменные now.year, self.yob поменял местами
  ```python
    def get_age(self):
        now = datetime.now()
        return now.year - self.yob
  ```
+ Метод set_name. Была допущена ошибка при присвоении имени.
  ```python
    def set_name(self, name):
        self.name = name
  ```
+ Методе set_address. В присвоении лишний знак
   ```python
    def set_address(self, address):
        self.address = address
   ```
+ Метод is_homeless. Был пропущен self и в аннотации стоят одинарные кавычки вместо двойных 
   ```python
    def is_homeless(self):
        return self.address is None
   ```
>> **Также методы можно упростить гетерами и сеттерами**