"""
D. Кружки

____________________________________________________________
| Ограничение времени  | 1 секунда                         |
| Ограничение памяти   | 64Mb                              |
| Ввод                 | стандартный ввод или input.txt    |
| Вывод                | стандартный вывод или output.txt  |
____________________________________________________________

В компании, где работает Тимофей, заботятся о досуге сотрудников и устраивают различные кружки по интересам.
Когда кто-то записывается на занятие, в лог вносится название кружка.

По записям в логе составьте список всех кружков, в которые ходит хотя бы один человек.


Формат ввода:
В первой строке даётся натуральное число n, не превосходящее 10 000 –— количество записей в логе.

В следующих n строках —– названия кружков.


Формат вывода:
Выведите уникальные названия кружков по одному на строке, в порядке появления во входных данных.
"""


# Функция main считывает число записей в логе n.
def main():
    n = int(input().strip())
    # Создаётся множество clubs для хранения уникальных названий кружков и список unique_clubs для
    # хранения уникальных названий кружков в порядке их появления.
    clubs = set()
    unique_clubs = []

    # В цикле проходит по всем записям в логе, считывая название кружка.
    for _ in range(n):
        club = input().strip()
        # Если название кружка отсутствует в множестве clubs, то добавляет его
        # в список unique_clubs и множество clubs.
        if club not in clubs:
            unique_clubs.append(club)
            clubs.add(club)
    # В конце выводит все уникальные названия кружков из списка unique_clubs по одному на строке.
    for club in unique_clubs:
        print(club)


if __name__ == '__main__':
    main()





