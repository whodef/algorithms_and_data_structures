"""
L. МногоГоша

_____________________________________________________________________________________________________
| Язык                    | Ограничение времени | Ограничение памяти |   Ввод        |   Вывод      |
_____________________________________________________________________________________________________
| Все языки               | 1 секунда           | 256Mb              |               |              |
| Python 3.7.3            | 2.5 секунд          | 256Mb              | стандартный   | стандартный  |
| OpenJDK Java 11         | 6 секунд            | 256Mb              | ввод или      | вывод или    |
| C# (MS .NET 6.0 + ASP)  | 6 секунд            | 256Mb              | input.txt     | output.txt   |
| GNU c++17 7.3           | 0.7 секунд          | 64Mb               |               |              |
| C# (MS .NET 5.0 + ASP)  | 6 секунд            | 256Mb              |               |              |
| GNU GCC 12.2 C++20      | 0.7 секунд          | 64Mb               |               |              |
_____________________________________________________________________________________________________

Дана длинная строка, состоящая из маленьких латинских букв. Нужно найти все её подстроки длины n,
которые встречаются хотя бы k раз.



Формат ввода:
В первой строчке через пробел записаны два натуральных числа n и k.

Во второй строчке записана строка, состоящая из маленьких латинских букв. Длина строки 1 ≤ L ≤ 106.

n ≤ L, k ≤ L.



Формат вывода:
Для каждой найденной подстроки выведите индекс начала её первого вхождения (нумерация в строке начинается с нуля).

Выводите индексы в любом порядке, в одну строку, через пробел.
"""
