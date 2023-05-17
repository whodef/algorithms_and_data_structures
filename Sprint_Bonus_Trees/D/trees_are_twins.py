"""
D. Деревья - близнецы

_____________________________________________________________
| Ограничение времени   | 1 секунда                         |
| Ограничение памяти    | 64Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________


Гоше на день рождения подарили два дерева. Тимофей сказал, что они совершенно одинаковые.
Но, по мнению Гоши, они отличаются.
Помогите разрешить этот философский спор!


Формат ввода:

На вход подаются корни двух деревьев.
Используйте заготовки кода для данной задачи.


Формат вывода:

Функция должна вернуть True если деревья являются близнецами. Иначе - False.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def are_trees_identical(root1, root2):
    """Проверяет, являются ли два дерева идентичными."""

    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        values_match = root1.value == root2.value
        left_subtrees_match = are_trees_identical(root1.left, root2.left)
        right_subtrees_match = are_trees_identical(root1.right, root2.right)

        return values_match and left_subtrees_match and right_subtrees_match

    return False


def solution(root1, root2):
    return are_trees_identical(root1, root2)


def test():
    node1 = Node(1)
    node2 = Node(2)
    root1 = Node(3, node1, node2)

    node3 = Node(1)
    node4 = Node(2)
    root2 = Node(3, node3, node4)

    assert solution(root1, root2)


if __name__ == '__main__':
    test()
