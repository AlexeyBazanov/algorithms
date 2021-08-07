"""
-- ID ПОСЫЛКИ - 52170417 --

-- ПРИНЦИП РАБОТЫ --
Для начала нам нужно привести переданный массив к бинарной куче.
Для этого поочередно сравним все элементы массива начиная с левым и правым потомком,
чтобы он соответствовал свойству бинарной кучи (ключ в любой вершине не меньше (если куча для максимума), чем значения её потомков).
После того как мы привели массив к бинарной куче, мы будем "извлекать" по одному элементы из массива начинаяя с конца
меняя их местами с первым, самым приоритетным элементом, на каждой итерации снова просеивая кучу.
В итоге массив окажется отсортированным.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Для первичного приобразования массива в кучу понадобится O(n) времени.
Для повторного просеивания понадобится O(n * log(n)) времени.
Итого O(n * log(n)).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для первоначального преобразования массива в кучу понадобится O(log n) доп памяти,
т.к. индекс массива при каждом рекурсивном вызове удваивается, пока не выйдет за границы массива.
Для повторного просеивания понадобится так же O(log n) доп памяти.
Итого понадобится O(log n) доп памяти.
"""
import sys


def to_heap(array, n, index):
    largest = index
    left = 2 * index + 1
    right = left + 1

    if left < n and is_first_student_better(array[index], array[left]):
        largest = left

    if right < n and is_first_student_better(array[largest], array[right]):
        largest = right

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        to_heap(array, n, largest)


def pyramid_sort(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        to_heap(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        to_heap(array, i, 0)


def is_first_student_better(student1, student2, name_key=0, tasks_key=1, penalty_key=2):
    if student1[tasks_key] == student2[tasks_key]:
        if student1[penalty_key] == student2[penalty_key]:
            return student1[name_key] < student2[name_key]
        return student1[penalty_key] < student2[penalty_key]
    return student1[tasks_key] > student2[tasks_key]


def print_score(name_key=0, tasks_key=1, penalty_key=2):
    students_number = int(sys.stdin.readline().strip())
    array = []

    for i in range(students_number):
        student_score = sys.stdin.readline().strip().split(' ')
        student_score[tasks_key] = int(student_score[tasks_key])
        student_score[penalty_key] = int(student_score[penalty_key])
        array.append(student_score)

    pyramid_sort(array)

    for i in range(students_number):
        print(array[i][name_key])


if __name__ == '__main__':
    print_score()