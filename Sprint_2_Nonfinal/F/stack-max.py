"""
F. Стек - Max

____________________________________________________________
| Ограничение времени  | 1 секунда                         |
| Ограничение памяти   | 64Mb                              |
| Ввод                 | стандартный ввод или input.txt    |
| Вывод                | стандартный вывод или output.txt  |
____________________________________________________________

Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().

Формат ввода:
В первой строке записано одно число n — количество команд, которое не превосходит 10000. В следующих n строках идут
команды. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

Формат вывода:
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max()
напечатайте «None». Если происходит удаление из пустого стека — напечатайте «error».
"""


class StackMax:
    def __init__(self):
        self.__items = []
        self.__max_stack = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        if self.is_empty() or item >= self.__max_stack[-1]:
            self.__max_stack.append(item)
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'

        removed = self.__items.pop()
        if removed == self.__max_stack[-1]:
            self.__max_stack.pop()

        if self.is_empty():
            self.__max_stack.clear()
        return removed

    def get_max(self):
        if self.is_empty():
            return 'None'
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackMax()
    n = int(input())
    result = []

    for idx in range(n):
        command = input().split()

        if command[0] == 'push':
            stack.push(int(command[1]))

        if command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')

        if command[0] == 'get_max':
            result.append(stack.get_max())

    for idx in result:
        print(idx)
