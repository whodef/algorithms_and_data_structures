"""
L. Лишняя буква

____________________________________________________________
| Ограничение времени  | 1 секунда                         |
| Ограничение памяти   | 64Mb                              |
| Ввод                 | стандартный ввод или input.txt    |
| Вывод                | стандартный вывод или output.txt  |
____________________________________________________________

Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

Формат ввода:
На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов.
Строки не бывают пустыми.

Формат вывода:
Выведите лишнюю букву.
"""

from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    ascii_sum_shorter = sum(ord(c) for c in shorter)
    ascii_sum_longer = sum(ord(c) for c in longer)
    return chr(ascii_sum_longer - ascii_sum_shorter)


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))


# Для решения этой задачи можно посчитать сумму кодов ASCII символов в строке longer и вычесть из нее сумму кодов
# символов в строке shorter. Разность будет равна коду ASCII лишнего символа.
# Наконец, преобразовать код в символ с помощью функции chr().