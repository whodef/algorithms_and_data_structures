"""
K. Сортировка слиянием

____________________________________________________________
| Ограничение времени |  2 секунды                         |
| Ограничение памяти  |  64Mb                              |
| Ввод                |  стандартный ввод или input.txt    |
| Вывод               |  стандартный вывод или output.txt  |
____________________________________________________________

Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше обязательно надо реализовать отдельно функцию
merge и функцию merge_sort.
Функция merge принимает два отсортированных массива, сливает их в один отсортированный массив и возвращает его.
Если требуемая сигнатура имеет вид merge(array, left, mid, right), то первый массив задаётся полуинтервалом [left, mid)
массива array, а второй – полуинтервалом [mid, right) массива array.
Функция merge_sort принимает некоторый подмассив, который нужно отсортировать. Подмассив задаётся полуинтервалом — его
началом и концом. Функция должна отсортировать передаваемый в неё подмассив, она ничего не возвращает.
Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно вызывает сортировку отдельно для каждой.
Затем два отсортированных массива сливаются в один с помощью merge.
Заметьте, что в функции передаются именно полуинтервалы [begin, end), то есть правый конец не включается. Например,
если вызвать merge_sort(arr, 0, 4), где arr = [4, 5, 3, 0, 1, 2], то будут отсортированы только первые четыре элемента,
изменённый массив будет выглядеть как arr = [0, 3, 4, 5, 1, 2].

Реализуйте эти две функции.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.

Формат ввода:
Передаваемый в функции массив состоит из целых чисел, не превосходящих по модулю 109. Длина сортируемого диапазона
не превосходит 105.

Формат вывода:
При написании и отправке решений соблюдайте следующие правила:
Отправляйте решение в виде файла. Если текст решения будет вставлен в форму, то будет возвращена ошибка.
В качестве компилятора выберите Make.

На Java назовите файл с решением Solution.java и реализуйте внутри класса указанные функции, для C# – Solution.cs
Для остальных решений не используйте в качестве имени файла слово solution
Укажите правильное разрешение для файла (.cpp, .java, .go. .js, .py). Для решений на C++ разрешение .h
не поддерживается.

Ниже приведены сигнатуры функций, которые необходимо реализовать, для различных языков программирования.
C++
using Iterator = std::vector<int>::iterator;
using CIterator = std::vector<int>::const_iterator;
std::vector<int> merge(CIterator left_begin, CIterator left_end,
                       CIterator right_begin, CIterator right_end);
void merge_sort(Iterator begin, Iterator end);
Java

public class Solution {
        public static int[] merge(int[] arr, int left, int mid, int right);
        public static void merge_sort(int[] arr, int left, int right);
}
Python

merge(arr: list, left: int, mid: int, right: int) -> array
merge_sort(arr: list, left: int, right: int) -> None
Go

package main
func merge(arr []int, lf int, mid int, rg int) []int
func merge_sort(arr []int, lf int, rg int)
JavaScript

merge :: (Array arr, Number lf, Number mid, Number rg) -> Array
merge_sort :: (Array arr, Number lf, Number rg) -> void
"""


def merge(arr, lf, mid, rg):
    # Your code
    # “ヽ(´▽｀)ノ”
    result = []
    left = arr[lf:mid]
    right = arr[mid:rg]
    ileft = iright = 0
    while len(result) < len(left) + len(right):
        if left[ileft] <= right[iright]:
            result.append(left[ileft])
            ileft += 1
        else:
            result.append(right[iright])
            iright += 1
        if iright == len(right):
            result += left[ileft:]
            break
        if ileft == len(left):
            result += right[iright:]
            break
    return result


def merge_sort(arr, lf, rg):
    # Your code
    # “ヽ(´▽｀)ノ”
    if rg - lf >= 2:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
