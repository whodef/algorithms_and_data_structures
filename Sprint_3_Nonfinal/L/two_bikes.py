"""
L. Два велосипеда

____________________________________________________________
| Ограничение времени |  1 секунда                         |
| Ограничение памяти  |  256Mb                             |
| Ввод                |  стандартный ввод или input.txt    |
| Вывод               |  стандартный вывод или output.txt  |
____________________________________________________________

Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, в которую каждый день
он может добавлять деньги (если, конечно, у него есть такая финансовая возможность). В процессе накопления
Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить:

- первый день, в которой Вася смог бы купить один велосипед.
- и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода:
В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания.
Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.

Формат вывода:
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.
"""


# Решение 2. Оптимизировано по DRY
def find_day(n, savings, bike_cost, k):
    if k * bike_cost > savings[n - 1]:
        return -1

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if savings[mid] < k * bike_cost:
            left = mid + 1
        else:
            right = mid - 1
    return left + 1

n = int(input())
savings = list(map(int, input().split()))
bike_cost = int(input())

first_day = find_day(n, savings, bike_cost, 1)
second_day = find_day(n, savings, bike_cost, 2)

print(first_day, second_day)


# Решение 1
#
# def find_first_day(n, savings, bike_cost):
#     if savings[0] >= bike_cost:
#         return 1
#
#     left = 0
#     right = n - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if savings[mid] < bike_cost:
#             left = mid + 1
#         else:
#             right = mid - 1
#     if left >= n:
#         return -1
#     else:
#         return left + 1
#
#
# def find_second_day(n, savings, bike_cost):
#     if savings[0] >= 2 * bike_cost:
#         return 1
#
#     left = 0
#     right = n - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if savings[mid] < 2 * bike_cost:
#             left = mid + 1
#         else:
#             right = mid - 1
#     if left >= n:
#         return -1
#     else:
#         return left + 1
#
#
# n = int(input())
# savings = list(map(int, input().split()))
# bike_cost = int(input())
#
# first_day = find_first_day(n, savings, bike_cost)
# second_day = find_second_day(n, savings, bike_cost)
#
# print(first_day, second_day)
