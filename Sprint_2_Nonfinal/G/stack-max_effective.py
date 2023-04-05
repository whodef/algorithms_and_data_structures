"""
G. Стек - MaxEffective

_____________________________________________________________________________________________________
| Язык                    | Ограничение времени | Ограничение памяти |   Ввод        |   Вывод      |
_____________________________________________________________________________________________________
| Все языки               | 0.2 секунды         | 64Mb               |               |              |
| Node.js 14.15.5         | 1.5 секунд          | 64Mb               |               |              |
| Python 3.7.3            | 1.5 секунд          | 64Mb               | стандартный   | стандартный  |
| OpenJDK Java 11         | 1.5 секунд          | 64Mb               | ввод или      | вывод или    |
| C# (MS .NET 6.0 + ASP)  | 1.5 секунд          | 64Mb               | input.txt     | output.txt   |
| Golang 1.20.1	          | 0.5 секунд          | 64Mb               |               |              |
| C# (MS .NET 5.0 + ASP)  | 1.5 секунд          | 64Mb               |               |              |
_____________________________________________________________________________________________________

Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке.
Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.


Формат ввода:
В первой строке записано одно число — количество команд, оно не превосходит 100000. Далее идут команды по одной в
строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».


Формат вывода:
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте
«None». Если происходит удаление из пустого стека — напечатайте «error».
"""
import sys


class StackMaxEffective:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, num: int):
        if not self.items or self.items[-1] < num:
            self.items.append(num)
        else:
            self.items.append(self.items[-1])

    def pop(self):
        self.items.pop()

    def get_max(self):
        return self.items[-1]


def read_input():
    n = int(input())
    commands = [sys.stdin.readline().strip().split(' ') for _ in range(n)]
    return commands


def solution(commands):
    result = []
    stack = StackMaxEffective()
    for command in commands:
        if command[0] == 'get_max':
            if stack:
                result.append(str(stack.get_max()))
            else:
                result.append('None')
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack:
                stack.pop()
            else:
               result.append('error')
    print('\n'.join(result))


if __name__ == '__main__':
    commands = read_input()
    solution(commands)
