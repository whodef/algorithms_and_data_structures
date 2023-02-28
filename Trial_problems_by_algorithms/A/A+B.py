"""
A. A+B


-------------------------------------------------------------
| Ограничение времени	 | 1 секунда                        |
-------------------------------------------------------------
| Ограничение памяти	 | 64Mb                             |
-------------------------------------------------------------
| Ввод	                 | стандартный ввод или input.txt   |
-------------------------------------------------------------
| Вывод                  | стандартный вывод или output.txt |
-------------------------------------------------------------


Это ваша первая задача. В ней вам придётся прочитать два числа и сложить их. Результат необходимо вывести на стандартный
поток вывода или в файл, указанный в условии задачи.
Рекомендуем воспользоваться заготовками кода для данной задачи, лежащими в репозитории курса
https://github.com/Yandex-Practicum/algorithms-templates


Формат ввода:
В первой строке задано первое число, во второй – второе. Оба числа лежат в диапазоне от
−10**9 до 10**9.

Формат вывода:
Выведите единственное число – результат сложения двух чисел.
"""

from typing import Tuple


def get_sum(a: int, b: int) -> int:
    return a + b


def read_input() -> Tuple[int, int]:
    a = int(input())
    b = int(input())
    return a, b


a, b = read_input()

print(get_sum(a, b))
