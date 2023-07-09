"""
1. Сконфигурируйте логгер программы из темы 4 так, чтобы он:

* писал логи в файл stderr.txt;
* не писал дату, но писал время в формате HH:MM:SS,
  где HH — часы, MM — минуты, SS — секунды с ведущими нулями.
  Например, 16:00:09;
* выводил логи уровня INFO и выше.

2. К нам пришли сотрудники отдела безопасности и сказали, что, согласно новым стандартам безопасности,
хорошим паролем считается такой пароль, который не содержит в себе слов английского языка,
так что нужно доработать программу из предыдущей задачи.

Напишите функцию is_strong_password, которая принимает на вход пароль в виде строки,
а возвращает булево значение, которое показывает, является ли пароль хорошим по новым стандартам безопасности.
"""

import getpass
import hashlib
import logging

logger = logging.getLogger("password_checker")

WORDS = []
LEN_WORD = {}

def is_strong_password(password: str) -> bool:
    if len(password) < 4:
        logger.warning("Вы ввели слишком слабый пароль")
        return True

    # for symbol in password:
    #     if symbol.isascii() and symbol.isalpha():
    #         logger.warning("Содержит буквы английского языка")
    #         return True

    if not WORDS:
        with open('/usr/share/dict/words', 'r') as file:
            # Сначала создаем список всех слов длиной больше 3 букв из словаря
            [WORDS.append(i.strip()) for i in file if len(i.strip()) > 3]
            # Создаем словарь, где ключ это длина слова, а значение список слов,
            # данной длины
            for word in WORDS:
                if not LEN_WORD.get(len(word), {}):
                    LEN_WORD[len(word)] = [word]
                else:
                    LEN_WORD[len(word)].append(word)

    # Проходимся по списку-значение словаря с ключем длины пароля
    password = password.lower()
    for i in LEN_WORD[len(password)]:
        if i.lower() == password:
            logger.warning("Содержит слова английского языка из словаря")
            return True


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass(prompt='Введите пароль: ')

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    elif is_strong_password(password):
        return False

    try:
        hasher = hashlib.md5()

        # hasher.update(password.encode("latin-1"))
        hasher.update(password.encode("cp1251"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, filename="stderr.txt",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S")
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)
