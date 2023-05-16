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

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    pass


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == '__main__':
    test()
