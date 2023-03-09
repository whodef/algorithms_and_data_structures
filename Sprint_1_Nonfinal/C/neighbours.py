"""
C. Соседи

___________________________________________________________
| Ограничение времени  | 1 секунда                        |
| Ограничение памяти   | 64Mb                             |
| Ввод                 | стандартный ввод или input.txt   |
| Вывод                | стандартный вывод или output.txt |
___________________________________________________________

Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент,
находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

Формат ввода:
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В последних двух
строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода:
Напечатайте нужные числа в возрастающем порядке через пробел.
"""

from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours = []

    # Индексы соседних элементов
    neighbours_indices = [
        (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
    ]

    # Добавляем соседние элементы, если они находятся в границах матрицы
    for r, c in neighbours_indices:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            neighbours.append(matrix[r][c])
    return sorted(neighbours)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(' '.join(map(str, get_neighbours(matrix, row, col))))