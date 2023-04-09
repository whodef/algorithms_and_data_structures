"""
C. Подпоследовательность

_____________________________________________________________________________________________________
| Язык                    | Ограничение времени | Ограничение памяти |   Ввод        |   Вывод      |
_____________________________________________________________________________________________________
| Все языки               | 0.1 секунда         | 64Mb               |               |              |
| Node.js 14.15.5         | 0.2 секунды         | 64Mb               |               |              |
| Python 3.7.3            | 0.12 секунд	        | 64Mb               | стандартный   | стандартный  |
| OpenJDK Java 11         | 0.3 секунды         | 64Mb               | ввод или      | вывод или    |
| C# (MS .NET 6.0 + ASP)  | 0.3 секунды         | 64Mb               | input.txt     | output.txt   |
| C# (MS .NET 5.0 + ASP)  | 0.3 секунды         | 64Mb               |               |              |
_____________________________________________________________________________________________________

Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно понять, является ли первая из них
подпоследовательностью второй. Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос,
просто посмотрев на них. Помогите Гоше написать функцию, которая решает эту задачу.

Формат ввода:
В первой строке записана строка s.

Во второй —- строка t.

Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000. Строки не могут быть пустыми.

Формат вывода:
Выведите True, если s является подпоследовательностью t, иначе —– False.
"""


def is_subsequence(s, t):
    i = 0
    for c in t:
        if i < len(s) and c == s[i]:
            i += 1
    return i == len(s)


s = input().strip()
t = input().strip()

print(is_subsequence(s, t))
