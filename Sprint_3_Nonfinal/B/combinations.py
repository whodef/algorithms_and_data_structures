"""
B. Комбинации

____________________________________________________________
| Ограничение времени |  1 секунда                         |
| Ограничение памяти  |  64Mb                              |
| Ввод                |  стандартный ввод или input.txt    |
| Вывод               |  стандартный вывод или output.txt  |
____________________________________________________________

На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв,
которые можно набрать такой последовательностью нажатий.

Формат ввода:
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

Формат вывода:
Выведите все возможные комбинации букв через пробел.
"""


def letter_combinations(digits):
    if not digits:
        return []

    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(combination, index):
        if index == len(digits):
            result.append(combination)
            return

        for letter in mapping[digits[index]]:
            backtrack(combination + letter, index + 1)

    result = []
    backtrack('', 0)
    return result


digits = input().strip()
combinations = letter_combinations(digits)
print(' '.join(combinations))
