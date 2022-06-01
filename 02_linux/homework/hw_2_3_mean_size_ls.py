"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
$ ls -l ./
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os
import subprocess


def get_mean_size(ls_output_path: str) -> float:
    with open(ls_output_path, mode='r', encoding='utf-8') as text:
        size = 0
        count = 0
        for line in text:
            if len(line.split()) == 9 and line.split()[0].startswith("-rw") and line.split()[4].isdigit():
                size += float(line.split()[4])
                count += 1
        return size / count


if __name__ == "__main__":
    output = "output_mean_size_ls.txt"
    subprocess.call(f"ls -l ./ > {output}", shell=True)
    path = os.path.abspath("output_mean_size_ls.txt")
    average_file_size = get_mean_size(path)
    from hw_2_2_ps_aux_rss import _sizeof_fmt
    avg = _sizeof_fmt(average_file_size)
    print("Средний размер файла:", avg)
