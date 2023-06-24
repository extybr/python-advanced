"""
Напишите код, который выводит сам себя.
Обратите внимание, что скрипт может быть расположен в любом месте.
"""
import sys

result = 0
for number in range(1, 11):
    result += number ** 2

# Secret magic code

with open(sys.argv[0]) as me:
    print(me.read())

# Secret magic code

# ver.2
code = """
result = 0
for number in range(1, 11):
    result += number ** 2
"""
print(code)
# ver.2

# ver.3
with open('self_printing.py', 'r', encoding='utf-8') as text:
    part = text.read()
    print(part[115:192])
# ver.3

# ver.4
s='s=%r;print(s%%s)';print(s%s)
# ver.4
