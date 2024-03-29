"""
G. Максимальный путь в дереве

_____________________________________________________________
| Ограничение времени   | 1 секунда                         |
| Ограничение памяти    | 64Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Тимофей устраивает соревнования по спортивному ориентированию в своём офисе. Схема офиса представлена в виде
дерева. Посещая каждый пункт, можно зарабатывать или терять очки. Если в узле записано положительное число, это
значение добавляется к текущему количеству очков участника. Если отрицательное —– очки вычитаются. Если
0 — их количество не меняется.

Нужно определить, какое максимальное число очков можно заработать, пройдя по пути из какого-то пункта A в какой-то
(возможно, тот же) пункт B.
Путь необязательно должен проходить через корень или содержать лист. Путь должен содержать по крайней мере один узел.


Пример 1:
В дереве всего три вершины, во всех вершинах записаны положительные числа, поэтому объединим все три вершины в
один путь. В ответе получим: 1 + 1 + 2 = 4.

Пример 2:
Теперь в дереве есть вершина с отрицательным весом, через неё в данном случае проходить будет невыгодно.
Оптимальный путь: 2 + 7 + 3 = 12.

Пример 3:
Оптимальный путь: 7 + 2 + 3 + 9 = 21.

Пример 4:
В этот раз имеет смысл пройти через вершину с отрицательным весом, так как в левом поддереве вершины −3 лежит 5.
Оптимальный путь: 2 + 2 − 3 + 5 = 6.
Требования к решению: передаваемое в качестве аргумента дерево нельзя менять. Не храните вспомогательную
информацию в вершинах.


Формат ввода:

На вход подается корень дерева.
Используйте заготовки кода для данной задачи.


Формат вывода:

Функция должна вернуть число, равное максимальному количеству очков, которое можно заработать,
попав из города А в город В.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.value)


def search_max_path(root, max_sum=None):
    """Функция рекурсивно обходит левое и правое поддерево текущего узла."""
    if root is None:
        return 0, max_sum

    left_max_sum, max_sum = search_max_path(root.left, max_sum)
    right_max_sum, max_sum = search_max_path(root.right, max_sum)

    branch_max_sum = max(max(left_max_sum, right_max_sum) + root.value, root.value)

    subtree_max_sum = max(branch_max_sum, left_max_sum + right_max_sum + root.value)

    if max_sum is None:
        max_sum = subtree_max_sum
    else:
        max_sum = max(subtree_max_sum, max_sum)

    return branch_max_sum, max_sum


def solution(root) -> int:
    _, max_tree_sum = search_max_path(root)
    return max_tree_sum


def test():
    node1 = Node(5)
    node2 = Node(1)
    node3 = Node(-3, node2, node1)
    node4 = Node(2)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == '__main__':
    test()
