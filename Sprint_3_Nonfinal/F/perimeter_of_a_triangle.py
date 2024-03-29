"""
F. Периметр треугольника

______________________________________________________________________________
|                      | Все языки        | Python 3.7.3   | GNU c++17 7.3   |
______________________________________________________________________________
| Ограничение времени  | 1 секунда        | 0.12 секунд    | 0.015 секунд    |
______________________________________________________________________________
| Ограничение памяти   | 64Mb             | 64Mb           | 64Mb            |
______________________________________________________________________________
| Ввод                 | стандартный ввод или input.txt                      |
______________________________________________________________________________
| Вывод                | стандартный вывод или output.txt                    |
______________________________________________________________________________

Перед сном Рита решила поиграть в игру на телефоне. Дан массив целых чисел, в котором каждый элемент обозначает
длину стороны треугольника. Нужно определить максимально возможный периметр треугольника, составленного из сторон
с длинами из заданного массива. Помогите Рите скорее закончить игру и пойти спать.

Напомним, что из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник, если выполнено неравенство
треугольника: c < a + b

Разберём пример:
даны длины сторон 6, 3, 3, 2. Попробуем в качестве наибольшей стороны выбрать 6. Неравенство треугольника не может
выполниться, так как остались 3, 3, 2 —– максимальная сумма из них равна 6.

Без шестёрки оставшиеся три отрезка уже образуют треугольник со сторонами 3, 3, 2. Неравенство выполняется:
3 < 3 + 2. Периметр равен 3 + 3 + 2 = 8.


Формат ввода:
В первой строке записано количество отрезков n, 3≤ n≤ 10000.

Во второй строке записано n неотрицательных чисел, не превосходящих 10 000, –— длины отрезков.


Формат вывода:
Нужно вывести одно число —– наибольший периметр треугольника.

Гарантируется, что тройка чисел, которая может образовать треугольник, всегда есть.
"""


def sort_find(array):
    for index in range(0, len(array) - 1):
        if array[index] < (array[index + 1] + array[index + 2]):
            return array[index] + array[index + 1] + array[index + 2]


if __name__ == '__main__':
    _ = int(input())
    array = [int(num) for num in input().split()]
    print(sort_find(sorted(array, reverse=True)))
