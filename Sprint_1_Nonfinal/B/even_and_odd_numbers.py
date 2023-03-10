"""
B. Чётные и нечётные числа

____________________________________________________________
| Ограничение времени  | 1 секунда                         |
| Ограничение памяти   | 64Mb                              |
| Ввод                 | стандартный ввод или input.txt    |
| Вывод                | стандартный вывод или output.txt  |
____________________________________________________________

Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода:
В первой строке записаны три случайных целых числа a, b и c. Числа не превосходят 109 по модулю.

Формат вывода:
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
"""


def check_parity(a: int, b: int, c: int) -> bool:
    return a % 2 == b % 2 == c % 2


def print_result(result: bool) -> None:
    if result:
        print('WIN')
    else:
        print('FAIL')


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))


# В данной задаче нужно определить, являются ли все три числа четными или нечетными. Мы можем использовать операцию
# взятия остатка от деления на 2 (оператор %) для определения четности числа: если остаток от деления равен 0,
# то число четное, иначе - нечетное. Затем мы можем проверить, равны ли все три числа по четности, и вернуть
# соответствующее значение.
