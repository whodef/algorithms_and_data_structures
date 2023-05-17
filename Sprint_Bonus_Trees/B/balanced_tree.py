"""
B. Сбалансированное дерево

_____________________________________________________________
| Ограничение времени   | 1 секунда                         |
| Ограничение памяти    | 64Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть про сбалансированные деревья.
Он решил написать функцию, которая определяет, сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое поддеревья каждой вершины отличаются по высоте не
больше, чем на единицу.



Формат ввода:

На вход функции подаётся корень бинарного дерева.

Замечания про отправку решений:
По умолчанию выбран компилятор make. Решение нужно отправлять в виде файла с расширением, которое
соответствует вашему языку программирования. Если вы пишете на Java, имя файла должно быть
Solution.java, для C# – Solution.cs. Для остальных языков назовите файл my_solution.ext,
заменив ext на необходимое расширение.

Используйте заготовки кода для данной задачи, расположенные по ссылкам.



Формат вывода:

Функция должна вернуть True, если дерево сбалансировано в соответствии с критерием из условия, иначе - False.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return f"Node({self.value})"


def check_tree_balance(root):
    """Проверяет балансировку поддерева и вычисляет его высоту."""
    is_balanced = True
    left_subtree_height = 0
    right_subtree_height = 0

    if root.left is None and root.right is None:
        return True, 1

    if root.left is not None:
        is_balanced, left_subtree_height = check_tree_balance(root.left)

    if is_balanced and root.right is not None:
        is_balanced, right_subtree_height = check_tree_balance(root.right)

    tree_height = max(left_subtree_height, right_subtree_height) + 1

    is_balanced = is_balanced and abs(left_subtree_height - right_subtree_height) <= 1

    return is_balanced, tree_height


def is_tree_balanced(root):
    """Проверяет балансировку дерева."""
    is_balanced, _ = check_tree_balance(root)
    return is_balanced


def test():
    """Тестирует функцию is_tree_balanced."""
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert is_tree_balanced(node5)


if __name__ == '__main__':
    test()
