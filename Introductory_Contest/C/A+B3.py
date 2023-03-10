"""
------------------------------------------------
| Ограничение времени	   | 2 секунды         |
| Ограничение памяти	   | 64Mb              |
| Ввод	                   | стандартный ввод  |
| Вывод	                   | стандартный вывод |
________________________________________________

Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно читать из стандартного ввода и
выводить ответ в стандартный вывод.

Формат ввода
Первая строка входа содержит числа A и B (-2 ⋅ 10**9 ≤ A, B ≤ 2 ⋅ 10**9) разделенные пробелом

Формат вывода
В единственной строке выхода выведите сумму чисел A+B
"""

a, b = input().split(' ')
print(int(a) + int(b))
