"""
C. Дерево - анаграмма

_____________________________________________________________
| Ограничение времени   | 1 секунда                         |
| Ограничение памяти    | 64Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________


Гоша и Алла играют в игру «Удивительные деревья». Помогите ребятам определить, является ли дерево, которое
им встретилось, деревом-анаграммой?
Дерево называется анаграммой, если оно симметрично относительно своего центра.



Формат ввода:

Напишите функцию, которая определяет, является ли дерево анаграммой.

На вход подаётся корень дерева.

Замечания про отправку решений:
По умолчанию выбран компилятор make. Решение нужно отправлять в виде файла с расширением, которое соответствует
вашему языку программирования. Если вы пишете на Java, имя файла должно быть Solution.java, для C# – Solution.cs.
Для остальных языков назовите файл my_solution.ext, заменив ext на необходимое расширение.

Используйте заготовки кода для данной задачи, расположенные по ссылкам.



Формат вывода:

Функция должна вернуть True если дерево является анаграммой. Иначе - False.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def are_trees_mirror_images(root1, root2):
    """Проверяет, являются ли два поддерева зеркальными
    изображениями друг друга.
    """
    values_match = root1.value == root2.value
    left_nodes_match = (root1.left is None and root2.right is None) or (
            root1.left is not None and root2.right is not None)
    right_nodes_match = (root1.right is None and root2.left is None) or (
            root1.right is not None and root2.left is not None)

    result = values_match and left_nodes_match and right_nodes_match

    if not result:
        return False

    if root1.left is not None:
        result = are_trees_mirror_images(root1.left, root2.right)

    if result and root1.right is not None:
        result = are_trees_mirror_images(root1.right, root2.left)

    return result


def solution(root):
    """Проверяет, является ли дерево симметричным."""
    if root.left is not None and root.right is not None:
        return are_trees_mirror_images(root.left, root.right)

    if root.left is None and root.right is None:
        return True
    else:
        return False
    pass


def test():
    """Тестирует функцию is_tree_symmetric."""
    node8 = Node(5, None, None)
    node1 = Node(3, None, None)
    node2 = Node(4, node8, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert not solution(node7)


if __name__ == '__main__':
    test()
