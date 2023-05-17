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


def compute_poly_hash(k, m, s) -> int:
    """Вычисляет полиномиальный хеш для строки s."""
    if len(s) == 0:
        return 0
    else:
        hash_value = ord(s[0])
        for i in range(1, len(s)):
            hash_value = (hash_value * k) % m + ord(s[i])
        return hash_value % m


def find_substrings(n, k, s):
    """Находит все подстроки длины n в строке s, которые
    встречаются хотя бы k раз.
    """
    if len(s) < n:
        print('0')
        return

    # Параметры для полиномиального хеширования
    poly_hash_mod = 2 ** 64
    poly_hash_base = 31
    base_power_n_minus_1 = pow(poly_hash_base, n - 1, poly_hash_mod)

    # Словарь для хранения хешей подстрок и их вхождений
    hash_table = {}

    # Список для хранения индексов подстрок, встречающихся k раз
    answer = []

    hash_value = 0
    for i in range(len(s) - n + 1):
        if i == 0:
            substring = s[0: n]
            hash_value = compute_poly_hash(poly_hash_base, poly_hash_mod, substring)
        else:
            a1k = (ord(s[i - 1]) * base_power_n_minus_1) % poly_hash_mod
            r1 = ((hash_value - a1k) * poly_hash_base) % poly_hash_mod
            hash_value = r1 + ord(s[i + n - 1])

        if hash_value in hash_table:
            hash_table[hash_value][1] += 1
        else:
            hash_table[hash_value] = [i, 1, False]

        if hash_table[hash_value][1] >= k and not hash_table[hash_value][2]:
            hash_table[hash_value][2] = True
            answer.append(hash_table[hash_value][0])

    print(*answer)


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    s = input()
    find_substrings(n, k, s)
