"""
K. Выведи диапазон

_____________________________________________________________
| Ограничение времени   | 3 секунды                         |
| Ограничение памяти    | 128Mb                             |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Напишите функцию, которая будет выводить по не убыванию все ключи от L до R включительно в заданном
бинарном дереве поиска.
Ключи в дереве могут повторяться. Решение должно иметь сложность O(h+k), где h — глубина дерева, k — число
элементов в ответе.
В данной задаче если в узле содержится ключ x, то другие ключи, равные x, могут быть как в правом, так и в
левом поддереве данного узла. (Дерево строил стажёр, так что ничего страшного).


Формат ввода:

На вход функции подаётся корень дерева и искомый ключ. Число вершин в дереве не превосходит 10^5. Ключи – натуральные
числа, не превосходящие 10^9. Гарантируется, что L ≤ R.
В итоговом решении не надо определять свою структуру / свой класс, описывающий вершину дерева.

Используйте заготовки кода для данной задачи.


Формат вывода:

Функция должна напечатать по не убыванию все ключи от L до R по одному в строке.
"""


class Node:
    """Class for a Node of a Binary Search Tree."""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def print_range(node: Node, lower: int, upper: int) -> None:
    """Print the values of the nodes that fall within the
    range [lower, upper].
    """
    result = []
    in_order_traversal(node, lower, upper, result)
    print(*result)


def in_order_traversal(node: Node, lower: int, upper: int, result: list) -> None:
    """Perform an in-order traversal of the tree, appending the values
    of the nodes that fall within the range [lower, upper] to the result list.
    """
    if node.value >= lower and node.left is not None:
        in_order_traversal(node.left, lower, upper, result)

    if lower <= node.value <= upper:
        result.append(node.value)

    if node.value <= upper and node.right is not None:
        in_order_traversal(node.right, lower, upper, result)


def test():
    n1 = Node(value=2)
    n2 = Node(value=1, right=n1)
    n3 = Node(value=8)
    n4 = Node(value=8, right=n3)
    n5 = Node(value=9, left=n4)
    n6 = Node(value=10, left=n5)
    root = Node(value=5, left=n2, right=n6)

    print_range(root, 2, 8)  # Expected output: 2 5 8 8


if __name__ == '__main__':
    test()
