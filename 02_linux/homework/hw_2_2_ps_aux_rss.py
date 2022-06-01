"""
С помощью команды ps можно посмотреть список процессов, запущенных текущим пользователем.
Особенно эта команда выразительна с флагами
    $ ps aux
Запустите эту команду, output сохраните в файл, например вот так
$ ps aux > output_file.txt
В этом файле вы найдёте информацию обо всех процессах, запущенных в системе.
В частности там есть информация о потребляемой процессами памяти - это столбец RSS .
Напишите в функцию python, которая будет на вход принимать путь до файла с output
и на выход возвращать суммарный объём потребляемой памяти в человеко-читаемом формате.
Это означает, что ответ надо будет перевести в байты, килобайты, мегабайты и тд.

Для перевода можете воспользоваться функцией _sizeof_fmt
"""
import os


def _sizeof_fmt(number, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(number) < 1024.0:
            return "%3.1f%s%s" % (number, unit, suffix)
        number /= 1024.0
    return "%.1f%s%s" % (number, "Yi", suffix)


def get_summary_rss(ps_output_file_path: str, file_name: str) -> str:
    for file in os.listdir(ps_output_file_path):
        if file == file_name:
            with open(file, mode='r', encoding='utf-8') as text:
                ram = 0
                for line in text:
                    if line.split()[5].isdigit():
                        ram += float(line.split()[5])
                return _sizeof_fmt(ram)


if __name__ == "__main__":
    path = "./"
    my_file = 'output_file.txt'
    print(get_summary_rss(path, my_file))
