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


class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = [None] * max_size
        self.front = 0
        self.back = 0
        self.size = 0

    def push_front(self, value):
        if self.size == self.max_size:
            raise LookupError('error')
        self.front = (self.front - 1) % self.max_size
        self.buffer[self.front] = value
        self.size += 1

    def push_back(self, value):
        if self.size == self.max_size:
            raise LookupError('error')
        self.buffer[self.back] = value
        self.back = (self.back + 1) % self.max_size
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise LookupError('error')
        value = self.buffer[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        if self.size == 0:
            raise LookupError('error')
        self.back = (self.back - 1) % self.max_size
        value = self.buffer[self.back]
        self.size -= 1
        return value


n = int(input())
m = int(input())

deque = Deque(m)

for i in range(n):
    command = input().split()
    if command[0] == 'push_back':
        deque.push_back(int(command[1]))
    elif command[0] == 'push_front':
        deque.push_front(int(command[1]))
    elif command[0] == 'pop_front':
        value = deque.pop_front()
        if value is not None:
            print(value)
    elif command[0] == 'pop_back':
        value = deque.pop_back()
        if value is not None:
            print(value)
