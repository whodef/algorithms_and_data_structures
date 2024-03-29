"""
E. Две фишки - 2

______________________________________________________________________
|                               | Все языки        | GNU c++17 7.3   |
______________________________________________________________________
| Ограничение времени	        | 1 секунда        | 0.2 секунды     |
______________________________________________________________________
| Ограничение памяти            | 256Mb	           | 64Mb            |
______________________________________________________________________
| Ввод	                        | стандартный ввод или input.txt     |
______________________________________________________________________
| Вывод	                        | стандартный вывод или output.txt   |
______________________________________________________________________

Обратите внимание на ограничения в этой задаче.

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Фишки лежат на столе в порядке неубывания очков на них. Сначала Гоша называет число k, затем Рита должна выбрать две
фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 105.

Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках Риты в диапазоне от -105 до 105.

В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».

"""


from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    left, right = 0, len(arr) - 1  # начальные значения указателей

    while left < right:
        current_sum = arr[left] + arr[right]  # текущая сумма двух значений
        if current_sum == target_sum:
            return arr[left], arr[right]  # возвращаем два значения, сумма которых равна k
        elif current_sum < target_sum:
            left += 1  # увеличиваем левый указатель, чтобы получить большее значение
        else:
            right -= 1  # уменьшаем правый указатель, чтобы получить меньшее значение

    return None  # если не найдено двух значений, сумма которых равна k, возвращаем None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())

    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(' '.join(map(str, result)))


arr, target_sum = read_input()

print_result(two_sum(arr, target_sum))

# Для решения этой задачи можно использовать два указателя: один указатель начинает с начала массива, а второй
# указатель начинает с конца массива. Затем мы будем сравнивать сумму двух значений, на которые указывают эти
# указатели, с заданным числом k. Если эта сумма равна k, мы возвращаем два значения, на которые указывают указатели.
# Если сумма меньше k, мы увеличиваем левый указатель, чтобы получить большее значение. Если сумма больше k,
# мы уменьшаем правый указатель, чтобы получить меньшее значение. Мы продолжаем этот процесс, пока не найдем
# два значения, сумма которых равна k, или пока указатели не пересекутся.
#
# Примечание: в данном решении мы использовали встроенную функцию map для преобразования списка значений в строку.
# Функция map применяет функцию str к каждому элементу списка и возвращает новый список со строковыми представлениями
# элементов. Затем мы использовали метод join для объединения строк в одну строку, разделенную пробелами.
