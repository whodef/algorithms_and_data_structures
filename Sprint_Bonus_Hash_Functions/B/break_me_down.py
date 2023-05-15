"""
B. Сломай меня

Гоша написал программу, которая сравнивает строки исключительно по их хешам. Если хеш равен, то и строки равны.
Тимофей увидел это безобразие и поручил вам сломать программу Гоши, чтобы остальным неповадно было.

В этой задаче вам надо будет лишь найти две различные строки, которые для заданной хеш-функции будут давать
одинаковое значение.

Гоша использует хеш-функцию для a = 1000 и m = 123 987 123.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.


Формат ввода:
В задаче единственный тест без ввода


Формат вывода:
Отправьте две строки, по одной в строке. Строки могут состоять только из маленьких латинских букв и не должны превышать
в длину 1000 знаков каждая. Код отправлять не требуется. Строки из примера использовать нельзя.


Пример вывода:

ezhgeljkablzwnvuwqvp

gbpdcvkumyfxillgnqrv
"""

import random
import string

a = 1000
m = 123_987_123


def polynomial_hash(s, a, m):
    hash_val = 0
    power_of_p = 1

    for char in s:
        hash_val = (hash_val + ord(char) * power_of_p) % m
        power_of_p = (power_of_p * a) % m

    return hash_val


letters = string.ascii_lowercase
hash_map = {}

while True:
    random_string = ''.join(random.choice(letters) for _ in range(20))
    hash_val = polynomial_hash(random_string[::-1], a, m)

    if hash_val not in hash_map:
        hash_map[hash_val] = random_string
    else:
        print(f'{random_string} - {hash_val}')
        break
