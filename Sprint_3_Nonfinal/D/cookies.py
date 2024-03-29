"""
D. Печеньки

___________________________________________________________________________________________________
| Язык                   | Ограничение времени | Ограничение памяти |  Ввод        |  Вывод       |
___________________________________________________________________________________________________
| Все языки              | 0.05 секунд         | 64Mb               |              |              |
| Node.js 14.15.5        | 0.08 секунд         | 64Mb               | стандартный  | стандартный  |
| Python 3.7.3           | 1.5 секунд          | 64Mb               | ввод или     | ввод или     |
| Oracle Java 8          | 0.4 секунды         | 64Mb               | input.txt    | output.txt   |
| OpenJDK Java 11        | 0.4 секунды         | 64Mb               |              |              |
| C# (MS .NET 6.0 + ASP) | 0.2 секунды         | 64Mb               |              |              |
| C# (MS .NET 5.0 + ASP) | 0.2 секунды         | 64Mb               |              |              |
___________________________________________________________________________________________________

К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.

Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка есть фактор жадности — минимальный
размер печенья, которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными в лучшем случае, когда они
действуют оптимально.

Каждый ребёнок может взять не больше одного печенья.


Формат ввода:
В первой строке записано n —– количество детей.

Во второй —– n чисел, разделённых пробелом, каждое из которых –— фактор жадности ребёнка. Это натуральные числа,
не превосходящие 1000.

В следующей строке записано число m –— количество печенек.

Далее —– m натуральных чисел, разделённых пробелом —– размеры печенек. Размеры печенек не превосходят 1000.

Оба числа n и m не превосходят 10000.


Формат вывода:
Нужно вывести одно число –— количество детей, которые останутся довольными
"""


if __name__ == '__main__':
    n = int(input())
    factors = list(map(int, input().split()))
    m = int(input())
    cookies = list(map(int, input().split()))

    factors.sort()
    cookies.sort()

    i = j = count = 0
    while i < n and j < m:
        if cookies[j] >= factors[i]:
            count += 1
            i += 1
        j += 1

    print(count)
