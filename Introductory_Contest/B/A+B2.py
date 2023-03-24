"""
______________________________________________________________
| Ограничение времени     | 2 секунды                        |
| Ограничение памяти      | 64Mb                             |
| Ввод                    | стандартный ввод или input.txt   |
| Вывод                   | стандартный вывод или output.txt |
______________________________________________________________

Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно читать из файла
и выводить ответ в файл.

Формат ввода
Первая строка входного файла содержит числа A и B (-2 ⋅ 109 ≤ A, B ≤ 2 ⋅ 109) разделенные пробелом

Формат вывода
В единственной строке выходного файла выведите сумму чисел A+B
"""

with open('input.txt') as sdtin_file:
   a, b = map(int, sdtin_file.read().split())

with open('output.txt', 'w') as sdtout_file:
   sdtout_file.write(str(a + b))
