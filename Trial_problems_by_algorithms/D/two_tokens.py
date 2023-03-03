"""
D. Две фишки

------------------------------------------------------------
| Ограничение времени	| 4 секунды                        |
------------------------------------------------------------
| Ограничение памяти	| 256Mb                            |
------------------------------------------------------------
| Ввод	                | стандартный ввод или input.txt   |
------------------------------------------------------------
| Вывод	                | стандартный вывод или output.txt |
------------------------------------------------------------


Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Сначала Гоша называет
число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.

Формат ввода:
В первой строке записано количество фишек n, 2 ≤ n ≤ 104.

Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от -105 до 105.

В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода:
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».
"""

from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    seen = set()

    for num in arr:
        complement = target_sum - num

        if complement in seen:
            return (complement, num)
        seen.add(num)

    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print('None')
    else:
        print(f'{result[0]} {result[1]}')


arr, target_sum = read_input()

print_result(two_sum(arr, target_sum))
