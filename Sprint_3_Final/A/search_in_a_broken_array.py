"""
A. Поиск в сломанном массиве

______________________________________________________________
|                      | Все языки        | Make             |
______________________________________________________________
| Ограничение времени  | 0.001 секунда    | 1.5 секунд       |
______________________________________________________________
| Ограничение памяти   | 64Mb             | 64Mb             |
______________________________________________________________
| Ввод                 | стандартный ввод или input.txt      |
______________________________________________________________
| Вывод                | стандартный вывод или output.txt    |
______________________________________________________________

Алла ошиблась при копировании из одной структуры данных в другую. Она хранила массив чисел в кольцевом буфере.
Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время. Алла скопировала
данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности.
Теперь массив не является отсортированным. Тем не менее нужно обеспечить возможность находить в нем элемент за O(log n).
Можно предполагать, что в массиве только уникальные элементы.

Задачу необходимо сдавать с компилятором Make, он выбран по умолчанию, других компиляторов в задаче нет. Решение
отправляется файлом. Требуемые сигнатуры функций лежат в заготовках кода на диске.

От вас требуется реализовать функцию, осуществляющую поиск в сломанном массиве. Файлы с заготовками кода,
содержащими сигнатуры функций и базовый тест для поддерживаемых языков, находятся на Яндекс.Диске по ссылке.
Обратите внимание, что считывать данные и выводить ответ не требуется.

Расширение файла должно соответствовать языку, на котором вы пишете (.cpp, .java, .go, .js, .py).
Если вы пишете на Java, назовите файл с решением Solution.java, для C# – Solution.cs. Для остальных языков
название может быть любым, кроме solution.ext, где ext – разрешение для вашего языка.


Формат ввода:
Функция принимает массив натуральных чисел и искомое число k. Длина массива не превосходит 10000. Элементы
массива и число k не превосходят по значению 10000.

В примерах:

В первой строке записано число n — длина массива.

Во второй строке записано положительное число k — искомый элемент.

Далее в строку через пробел записано n натуральных чисел – элементы массива.


Формат вывода:
Функция должна вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля).
Если элемент не найден, функция должна вернуть −1.
Изменять массив нельзя.

Для отсечения неэффективных решений ваша функция будет запускаться от 100000 до 1000000 раз.
"""


def broken_search(arr, k):
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0 if arr[0] == k else -1

    # Поиск индекса pivot
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    pivot = left

    # Бинарный поиск элемента k
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        real_mid = (mid + pivot) % n
        if arr[real_mid] == k:
            return real_mid
        elif arr[real_mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    count_array = int(input())
    k = int(input())
    arr = [int(num) for num in input().split()]

    print(broken_search(arr, k))


# Решение 1
#
# def broken_search(arr, k):
#     n = len(arr)
#     if n == 0:
#         return -1
#     if n == 1:
#         return 0 if arr[0] == k else -1
#
#     # Поиск индекса pivot
#     left, right = 0, n - 1
#     while left < right:
#         mid = (left + right) // 2
#         if arr[left] < arr[right]:
#             # Массив уже отсортирован
#             pivot = left
#             break
#         elif arr[mid] > arr[right]:
#             left = mid + 1
#         elif arr[mid] < arr[right]:
#             right = mid
#         else:
#             right -= 1
#
#     else:
#         # Если цикл завершился по условию, а не по break,
#         # значит все элементы массива равны
#         pivot = left
#
#     # Бинарный поиск в одной из двух отсортированных частей
#     left, right = 0, n - 1
#     if arr[pivot] <= k <= arr[right]:
#         left = pivot
#     else:
#         right = pivot - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == k:
#             return mid
#         elif arr[mid] < k:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
#
#
# if __name__ == '__main__':
#     count_array = int(input())
#     k = int(input())
#     arr = [int(num) for num in input().split()]
#
#     print(broken_search(arr, k))
