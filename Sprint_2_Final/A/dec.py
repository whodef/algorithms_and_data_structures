"""
A. Дек

___________________________________________________________________________________________________
| Язык                  | Ограничение времени | Ограничение памяти |   Ввод        |   Вывод      |
___________________________________________________________________________________________________
| Все языки             | 0.3 секунды         | 39Mb               |               |              |
| Node.js 14.15.5       | 1 секунда           | 64Mb               |               |              |
| Python 3.7.3          | 2 секунды           | 64Mb               | стандартный   | стандартный  |
| C# (MS .Net 5.0)+ASP  | 1 секунда           | 64Mb               | ввод или      | вывод или    |
| Oracle Java 8         | 1 секунда           | 128Mb              | input.txt     | output.txt   |
| OpenJDK Java 11       | 1 секунда           | 128Mb              |               |              |
| Node JS 8.16          | 1 секунда           | 64Mb               |               |              |
___________________________________________________________________________________________________

Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x),
push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала
очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода:
В первой строке записано количество команд n — целое число, не превосходящее 100000. Во второй строке записано
число m — максимальный размер дека. Он не превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится макс-ное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится макс-ное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Формат вывода:
Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x)
ничего выводить не надо.
"""


# Решение
# ID успешной посылки: 84437920
# Address: https://contest.yandex.ru/contest/23390/run-report/84437920/
from typing import List, Tuple, Union


def solution(deque_max_size: int, commands: List[List[str]]) -> List[Union[str, int]]:
    results = []
    front, back = [], []

    def push_front(value: int):
        if len(front) + len(back) == deque_max_size:
            raise LookupError('error')
        front.append(value)

    def push_back(value: int):
        if len(front) + len(back) == deque_max_size:
            raise LookupError('error')
        back.append(value)

    def pop_front() -> int:
        if not front and not back:
            raise LookupError('error')
        if not front:
            front.extend(reversed(back))
            back.clear()
        return front.pop()

    def pop_back() -> int:
        if not front and not back:
            raise LookupError('error')
        if not back:
            back.extend(reversed(front))
            front.clear()
        return back.pop()

    for command, *args in commands:
        try:
            if command == 'push_front':
                push_front(int(args[0]))
            elif command == 'push_back':
                push_back(int(args[0]))
            elif command == 'pop_front':
                results.append(pop_front())
            elif command == 'pop_back':
                results.append(pop_back())
            else:
                raise ValueError(f'Unknown command "{command}"')
        except LookupError:
            results.append('error')

    return results


def read_input() -> Tuple[int, List[List[str]]]:
    command_amount = int(input())
    max_size = int(input())
    commands = [input().split(' ') for _ in range(command_amount)]
    return max_size, commands


if __name__ == '__main__':
    deque_max_size, commands = read_input()
    print('\n'.join(map(str, solution(deque_max_size, commands))))
