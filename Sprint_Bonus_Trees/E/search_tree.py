"""
E. Дерево поиска

_____________________________________________________________
| Ограничение времени   | 1 секунда                         |
| Ограничение памяти    | 64Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Гоша понял, что такое дерево поиска, и захотел написать функцию, которая определяет, является ли
заданное дерево деревом поиска. Значения в левом поддереве должны быть строго меньше, в правом —
строго больше значения в узле.

Помогите Гоше с реализацией этого алгоритма.


Формат ввода:

На вход функции подается корень бинарного дерева.
Используйте заготовки кода для данной задачи.


Формат вывода:

Функция должна вернуть True, если дерево является деревом поиска, иначе - False.
"""


class Node:
    def __init__(self, value: int = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(root: Node, min_val=float('-inf'), max_val=float('inf')):
    """Проверяет, является ли данное дерево бинарным деревом поиска."""
    if root is None:
        return True

    if not min_val < root.value < max_val:
        return False

    return is_bst(root.left, min_val, root.value) and is_bst(root.right, root.value, max_val)


def solution(root: Node) -> bool:
    return is_bst(root)


def test():
    node1 = Node(1)
    node2 = Node(4)
    node3 = Node(3, node1, node2)
    node4 = Node(8)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
