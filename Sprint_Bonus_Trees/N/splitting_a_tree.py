"""
N. Разбиение дерева

_____________________________________________________________
| Ограничение времени   | 2.5 секунд                        |
| Ограничение памяти    | 128Mb                             |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Дано бинарное дерево поиска, в котором хранятся целые числа. От этого дерева надо отделить k
самых маленьких элементов.

Реализуйте функцию, которая принимает корень дерева и число k, а возвращает два BST — в первом
k наименьших элементов из исходного дерева, а во втором — оставшиеся вершины BST.

В вершинах дерева уже записаны корректные размеры поддеревьев (точное название поля смотрите в
заготовках кода). После разбиения размеры должны остаться корректными — вам придётся пересчитывать их на ходу.

Ваше решение должно иметь асимптотику O(h), где h — высота исходного дерева.


Формат ввода:

Числа, записанные в вершинах дерева, лежат в диапазоне от 0 до 10^9. Дерево не содержит одинаковых ключей.
Число вершин в дереве не превосходит 10^5.
"""


# class Node:
#     def __init__(self, left=None, right=None, value=0, size=0):
#         self.right = right
#         self.left = left
#         self.value = value
#         self.size = size
#
#
# def update_size(node):
#     if node:
#         node.size = get_size(node.left) + get_size(node.right) + 1
#
#
# def get_size(node):
#     return node.size if node else 0
#
#
# def split(root, k):
#     if root is None:
#         return None, None
#
#     # If the size of the left subtree is greater than k, we know that the
#     # node we're looking for is in the left subtree.
#     if get_size(root.left) >= k:
#         # Split the left subtree.
#         left, root.left = split(root.left, k)
#         update_size(root)
#         return left, root
#     else:
#         # Otherwise, it's in the right subtree.
#         right, root.right = split(root.right, k - get_size(root.left) - 1)
#         update_size(root)
#         return root, right
#
#
# def test():
#     node1 = Node(None, None, 3, 1)
#     node2 = Node(None, node1, 2, 2)
#     node3 = Node(None, None, 8, 1)
#     node4 = Node(None, None, 11, 1)
#     node5 = Node(node3, node4, 10, 3)
#     node6 = Node(node2, node5, 5, 6)
#     left, right = split(node6, 4)
#     assert (left.size == 4)
#     assert (right.size == 2)
#
#
# if __name__ == '__main__':
#     test()
