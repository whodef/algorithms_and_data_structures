"""
A. Ближайший ноль

__________________________________________________________________________________________________________
| Язык                  | Ограничение времени  |  Ограничение памяти  |  Ввод           |  Вывод         |
__________________________________________________________________________________________________________
| Все языки             | 3 секунды            |  256Mb               |                 |                |
| Node.js 14.15.5       | 1.6 секунд           |  256Mb               |  стандартный    |  стандартный   |
| C# (MS .Net 5.0)+ASP	| 1.6 секунд           |  400Mb               |  ввод или       |  ввод или      |
| OpenJDK Java 11       | 1.6 секунд           |  400Mb               |  input.txt      |  output.txt    |
| Golang 1.16           | 0.8 секунды          |  64Mb                |                 |                |
| Kotlin 1.8.0 (JRE 11) | 2.5 секунд           |  256Mb               |                 |                |
| GNU c++17 7.3         | 0.8 секунд           |  64Mb                |                 |                |
__________________________________________________________________________________________________________

Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n
одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать
расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до
самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались
в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода:
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера
домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода:
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
"""

# Решение 3
from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    street_length = int(input())
    building_numbers = list(map(int, input().strip().split()))
    return street_length, building_numbers


def calculate_distances(street_length: int, building_numbers: List[int]) -> List[int]:
    left_distance = [float('inf')] * street_length
    cur = -float('inf')

    for i in range(street_length):
        if building_numbers[i] == 0:
            cur = i
        left_distance[i] = i - cur

    right_distance = [float('inf')] * street_length
    cur = float('inf')

    for i in reversed(range(street_length)):
        if building_numbers[i] == 0:
            cur = i
        right_distance[i] = cur - i

    distances = [
        min(left_distance[i], right_distance[i]) for i in range(street_length)
    ]
    return distances


if __name__ == '__main__':
    street_length = int(input())
    building_numbers = list(map(int, input().split()))
    distances = calculate_distances(street_length, building_numbers)
    print(*distances)


# Решение 2, переписать после ревью
#
# street_length = int(input())
# building_numbers = list(map(int, input().split()))
#
# left_distance = [float('inf')] * street_length
# cur = -float('inf')
#
# for i in range(street_length):
#     if building_numbers[i] == 0:
#         cur = i
#     left_distance[i] = i - cur
#
# right_distance = [float('inf')] * street_length
# cur = float('inf')
#
# for i in range(street_length - 1, -1, -1):
#     if building_numbers[i] == 0:
#         cur = i
#     right_distance[i] = cur - i
#
# distances = [
#     min(left_distance[i], right_distance[i]) for i in range(street_length)
# ]
# print(*distances)


# Решение 1, используя наивный алгоритм
# Превышен лимит времени исполнения
#
# n = int(input())
# houses = list(map(int, input().split()))
#
# for i in range(n):
#     if houses[i] == 0:
#         print(0, end=' ')
#     else:
#         left, right = i - 1, i + 1
#         while left >= 0 and houses[left] != 0:
#             left -= 1
#         while right < n and houses[right] != 0:
#             right += 1
#         if left < 0:
#             print(right - i, end=' ')
#         elif right >= n:
#             print(i - left, end=' ')
#         else:
#             print(min(i - left, right - i), end=' ')
