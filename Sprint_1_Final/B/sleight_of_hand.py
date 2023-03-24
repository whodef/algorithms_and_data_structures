"""
B. Ловкость рук

____________________________________________________________
| Ограничение времени  | 1 секунда                         |
| Ограничение памяти   | 64Mb                              |
| Ввод                 | стандартный ввод или input.txt    |
| Вывод                | стандартный вывод или output.txt  |
____________________________________________________________

Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4. В нём на каждом раунде появляется
конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут
нажать в один момент времени на k клавиш каждый. Если в момент времени t нажаты все нужные клавиши,
то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.

Формат ввода:
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра -— по 4 символа в каждой строке. Каждый символ – либо точка,
либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

Формат вывода:
Выведите единственное число -— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.
"""

# Решение 2

from typing import List, Tuple
from collections import Counter


def read_input() -> Tuple[int, List[str]]:
    keys_push = int(input()) * 2
    field_keys = [c for _ in range(4) for c in input().strip()]
    return keys_push, field_keys


def find_num_points(keys_push: int, field_keys: List[str]) -> int:
    counter = Counter(field_keys)
    keys = set(k for k in counter.keys() if k.isnumeric())
    num_points = sum(counter[k] <= keys_push for k in keys)
    return num_points


if __name__ == '__main__':
    keys_push, field_keys = read_input()
    print(find_num_points(keys_push, field_keys), sep='')


# Решение 1, после ревью необходимо было переписать
#
# from typing import List, Tuple
#
#
# def read_input() -> Tuple[int, List[str]]:
#     keys_push = int(input()) * 2
#     field_keys = [c for _ in range(4) for c in input().strip()]
#     return keys_push, field_keys
#
#
# def find_num_points(keys_push: int, field_keys: List[str]) -> int:
#     keys = set(k for k in field_keys if not k == '.')
#     num_points = sum(field_keys.count(k) <= keys_push for k in keys)
#     return num_points
#
#
# if __name__ == '__main__':
#     keys_push, field_keys = read_input()
#     print(find_num_points(keys_push, field_keys), sep='')
