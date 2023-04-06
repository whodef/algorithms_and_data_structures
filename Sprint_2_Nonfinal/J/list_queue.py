"""
J. Списочная очередь

____________________________________________________________
| Ограничение времени  | 0.3 секунды                       |
| Ограничение памяти   | 64Mb                              |
| Ввод                 | стандартный ввод или input.txt    |
| Вывод                | стандартный вывод или output.txt  |
____________________________________________________________

Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка. Помогите ему с реализацией.

Очередь должна поддерживать выполнение трёх команд:
- get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
- put(x) — добавить число x в очередь
- size() — вывести текущий размер очереди

Формат ввода:
В первой строке записано количество команд n — целое число, не превосходящее 1000. В каждой из следующих n строк
записаны команды по одной строке.

Формат вывода:
Выведите ответ на каждый запрос по одному в строке.
"""


class QueueList:
    def __init__(self, value=None, next_item=None, last_item=None):
        self.value = value
        self.next_item = next_item
        self.last_item = last_item
        self.queue_size = 0

    def get(self):
        current_value = self.value
        if self.next_item:
            self.value = self.next_item.value
            self.next_item = self.next_item.next_item
            self.queue_size -= 1
        else:
            self.value = None
            self.queue_size = 0

        return current_value

    def put(self, x):
        if not self.value:
            self.value = x
            self.last_item = self
        elif not self.next_item:
            self.next_item = QueueList(x)
            self.last_item = self.next_item
        else:
            self.last_item.next_item = QueueList(x)
            self.last_item = self.last_item.next_item
        self.queue_size += 1

    def size(self):
        return self.queue_size


def solution(commands):
    result: list = []
    queue = QueueList()

    for command in commands:
        if command[0] == 'put':
            queue.put(command[1])

        if command[0] == 'get':
            if queue.size() == 0:
                print('error')
            else:
                print(queue.get())

        if command[0] == 'size':
            print(queue.size())


def read_input():
    command_amount = int(input())
    commands = [input().split() for _ in range(command_amount)]
    return commands


if __name__ == '__main__':
    commands = read_input()
    solution(commands)
