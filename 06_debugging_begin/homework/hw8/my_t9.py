"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
from typing import List

LETTER = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv',
          9: 'wxyz'}
BACK = {i: j for j, i in LETTER.items()}


def my_t9(input_numbers: str) -> List[str]:
    right_words = []
    length = len(input_numbers)
    with open('/usr/share/dict/words', 'r', encoding='utf-8') as dictionary:
        for line in dictionary:
            word = line.strip()
            line_numbers = ''
            for letter in word[:length]:
                for key in BACK.keys():
                    if letter in key:
                        line_numbers += str(BACK[key])
            if len(word) >= length and input_numbers == line_numbers:
                right_words.append(word)
    return right_words


if __name__ == '__main__':
    numbers: str = input()
    # numbers = '9663'
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
