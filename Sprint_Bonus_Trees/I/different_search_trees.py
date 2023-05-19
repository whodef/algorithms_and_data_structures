"""
I. Разные деревья поиска

_____________________________________________________________
| Ограничение времени   | 5 секунд                          |
| Ограничение памяти    | 64Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Ребятам стало интересно, сколько может быть различных деревьев поиска, содержащих в своих узлах все уникальные
числа от 1 до n. Помогите им найти ответ на этот вопрос.


Формат ввода:

В единственной строке задано число n. Оно не превосходит 20.


Формат вывода:

Нужно вывести число, равное количеству различных деревьев поиска, в узлах которых могут быть размещены числа
от 1 до n включительно.
"""

import math


def main():
    nodes = int(input())

    print(catalan_number(nodes))


def catalan_number(n: int) -> int:
    return int(math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1)))


if __name__ == '__main__':
    main()