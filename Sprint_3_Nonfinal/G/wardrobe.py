"""
G. Гардероб

______________________________________________________________
|                      | Все языки        | OpenJDK Java 11  |
______________________________________________________________
| Ограничение времени  | 1 секунда        | 2 секунды        |
______________________________________________________________
| Ограничение памяти   | 128Mb            | 192Mb            |
______________________________________________________________
| Ввод                 | стандартный ввод или input.txt      |
______________________________________________________________
| Вывод                | стандартный вывод или output.txt    |
______________________________________________________________

Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового. После того как вещи других
расцветок были убраны, Рита захотела отсортировать свой новый гардероб по цветам. Сначала должны идти вещи розового
цвета, потом —– жёлтого, и в конце —– малинового. Помогите Рите справиться с этой задачей.

Примечание: попробуйте решить задачу за один проход по массиву!

Формат ввода:
В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000. Во второй строке даётся
массив, в котором указан цвет для каждого предмета. Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.

Формат вывода:
Нужно вывести в строку через пробел цвета предметов в правильном порядке.
"""


# Решение 4
from typing import Tuple


def swap(a: int, b: int) -> Tuple[int, int]:
    return b, a


if __name__ == '__main__':
    n = int(input())
    items = [int(x) for x in input().split()]

    left, right = 0, n - 1
    while items[left] == 0:
        left += 1
    while items[right] == 2:
        right -= 1

    i = left
    while i <= right:
        if items[i] == 0:
            items[i], items[left] = swap(items[i], items[left])
            left += 1
            i += 1
        elif items[i] == 2:
            items[i], items[right] = swap(items[i], items[right])
            right -= 1
        else:
            i += 1

    print(*items)


# Решение 3

if __name__ == '__main__':
    n = int(input())
    items = list(map(int, input().split()))

    left = 0  # левая граница для розового цвета
    right = n - 1  # правая граница для малинового цвета
    i = 0  # текущий индекс

    while i <= right:
        if items[i] == 0:
            items[i], items[left] = items[left], items[i]
            left += 1
            i += 1
        elif items[i] == 2:
            items[i], items[right] = items[right], items[i]
            right -= 1
        else:
            i += 1

    print(*items)

# Решение 2

# def counting_sort(array, k=3):
#     if len(array) == 0:
#         print(*array)
#
#     counted_values = [0] * k
#     counted_values[0] = array.count(0)
#     counted_values[1] = array.count(1)
#     counted_values[2] = array.count(2)
#     index = 0
#
#     for value in range(k):
#         for _ in range(0, counted_values[value]):
#             array[index] = value
#             index += 1
#
#     print(*array)
#
#
# if __name__ == '__main__':
#     _ = int(input())
#     array = [int(num) for num in input().split()]
#     counting_sort(array)


# Решение 1, не оптимизированное
#
# n = int(input())
# items = list(map(int, input().split()))
#
# count = [0, 0, 0]  # массив для подсчета количества вещей каждого цвета
# for item in items:
#     count[item] += 1
#
# result = []
# for color in [0, 1, 2]:  # проходим по цветам в нужном порядке
#     result.extend([color] * count[color])  # добавляем вещи нужного цвета в результат
#
# print(*result)  # выводим результат через пробел
