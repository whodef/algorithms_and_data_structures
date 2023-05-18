"""

_____________________________________________________________
| Ограничение времени   | 1 секунда                         |
| Ограничение памяти    | 64Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Вася и его друзья решили поиграть в игру. Дано дерево, в узлах которого записаны цифры от 0 до 9. Таким
образом, каждый путь от корня до листа содержит число, получившееся конкатенацией цифр пути (склеиванием
цифр пути в одно число). Нужно найти сумму всех таких чисел в дереве.

Гарантируется, что ответ не превосходит 20 000.


Формат ввода:

На вход подается корень дерева.
Используйте заготовки кода для данной задачи.


Формат вывода:

Функция должна вернуть число, равное сумме чисел всех путей в дереве.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def calculate_paths(root, path_sum=0):
    if root is None:
        return 0

    # Update the path sum
    path_sum = path_sum * 10 + root.value

    # If this is a leaf node, return the path sum
    if root.left is None and root.right is None:
        return path_sum

    # Otherwise, compute the path sums of the left and right subtrees
    return calculate_paths(root.left, path_sum) + calculate_paths(root.right, path_sum)


def solution(root) -> int:
    return calculate_paths(root)


def test():
    node1 = Node(2)
    node2 = Node(1)
    node3 = Node(3, node1, node2)
    node4 = Node(2)
    node5 = Node(1, node4, node3)
    assert solution(node5) == 275


if __name__ == '__main__':
    test()
