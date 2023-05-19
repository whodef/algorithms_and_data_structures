"""
L. Просеивание вниз

_____________________________________________________________
| Ограничение времени   | 2 секунды                         |
| Ограничение памяти    | 80Mb                              |
| Ввод                  | стандартный ввод или input.txt    |
| Вывод                 | стандартный вывод или output.txt  |
_____________________________________________________________

Напишите функцию, совершающую просеивание вниз в куче на максимум. Гарантируется, что порядок элементов
в куче может быть нарушен только элементом, от которого запускается просеивание.

Функция принимает в качестве аргументов массив, в нём хранятся элементы кучи, и индекс элемента, от
которого надо сделать просеивание вниз. Функция должна вернуть индекс, на котором элемент оказался после
просеивания. Также необходимо изменить порядок элементов в переданном в функцию массиве.

Индексация в массиве, содержащем кучу, начинается с единицы. Таким образом, сыновья вершины на
позиции v это 2v и 2v + 1. Обратите внимание, что нулевой элемент в передаваемом массиве фиктивный,
вершина кучи соответствует 1-му элементу.


Формат ввода:

Элементы кучи — целые числа, лежащие в диапазоне от −10^9 до 10^9. Все элементы кучи уникальны. Передаваемый в
функцию индекс лежит в диапазоне от 1 до размера передаваемого массива. В куче содержится от 1 до 10^5 элементов.

Используйте заготовки кода для данной задачи.
"""


def sift_down(heap, index) -> int:
    """Function to move the element at index down the heap until 
    it's in a valid spot.
    """
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # Check if left child and right child exist.
    left_exists = left_child_index < len(heap)
    right_exists = right_child_index < len(heap)

    if not left_exists and not right_exists:
        return index

    # Find the index of the larger child.
    if left_exists and right_exists:
        largest_child_index = left_child_index if heap[left_child_index] > heap[right_child_index] else right_child_index
    elif left_exists:
        largest_child_index = left_child_index
    else:
        largest_child_index = right_child_index

    # If the current node is smaller than its largest child, swap them.
    if heap[index] < heap[largest_child_index]:
        heap[index], heap[largest_child_index] = heap[largest_child_index], heap[index]
        return sift_down(heap, largest_child_index)
    else:
        return index


def test():
    # sample = [-1, 12, 1, 8, 3, 4, 7]
    sample = [-1, 12, 4, 7, 3, 1, 8]
    assert sift_down(sample, 3) == 6


if __name__ == '__main__':
    test()
