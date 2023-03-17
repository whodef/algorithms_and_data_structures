"""
A. Дек

________________________________________________________________________________________________________
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.3 секунды	39Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	1 секунда	64Mb
Python 3.7.3	2 секунды	64Mb
C# (MS .Net 5.0)+ASP	1 секунда	64Mb
Oracle Java 8	1 секунда	128Mb
OpenJDK Java 11	1 секунда	128Mb
Node JS 8.16	1 секунда	64Mb


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


