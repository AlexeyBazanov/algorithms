import sys

"""
-- ID ПОСЫЛКИ- 51798130 --

-- ПРИНЦИП РАБОТЫ --
Суть алгоритма такая же, как в быстрой сортироке, описанной в материалах практикума. 
Только для экономии памяти вместо сохранения кусков массива в памяти, 
в рекурсивный вызов функции передаются указатели начала и конца сортировки. 
Чтобы определить опорный элемент для дальнейшего рекурсивного вызова, 
мы используем функцию, в которую передаем индексы левой и правой границы поиска.
В этой функции мы определяем середину переданного нам интервала.
Слева от центрального элемента у нас должны остаться элементы меньше его.
Справа, соответственно, - элементы больше центрального. 
Для этого мы пробегаемся по всем элементам справа и слева, инкрементируя и декрементируя их индексы,
и в случае несоответствия позиций, меняем их местами.
Получившаяся в результате правая граница массива 
будет использована как индекс опорного элемента для рекурсивного вызова. 

Для сравнения элементов я использовал коллбэк функцию. 
По умолчанию она сработает на простом числовом массиве. 
Но для решения конкретно этой задачи нам надо сравнивать 3 элемента в списке:
рейтинг, штрафы и имя, для чего я создал отдельную функцию. 

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Средняя сложность работы данного алгоритма - O(N*logN).
В худшем случае - O(n^2).   

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Почитал статьи, и не совсем понял как определить пространственную сложность данной сортировки.
С одной стороны алгоритм не выделяет память на дополнительные подмассивы. 
В связи с этим можно считать, что алгоритм выполняется "на месте" и имеет пространственную сложность O(1).
Но так же алгоритму необходимо выделить дополнительную память на указатели на каждом уровне стека вызовов. 
Стек будет варьироваться от log(N) до N. 
Следовательно и памяти потребуется O(log(N)) в среднем и O(n) в худшем случае. 
"""


def sort(array, compare_func=lambda x, y: x > y):
    return quick_sort(array, 0, len(array) - 1, compare_func)


def quick_sort(array, left, right, compare_func):
    if left < right:
        pivot = partition(array, left, right, compare_func)
        quick_sort(array, left, pivot, compare_func)
        quick_sort(array, pivot + 1, right, compare_func)


def partition(array, left, right, compare_func):
    pivot = array[(left + right) // 2]
    cur_left = left
    cur_right = right
    # 8 3 2 5 1 9 7 2
    while cur_left <= cur_right:
        while compare_func(pivot, array[cur_left]):
            cur_left += 1
        while compare_func(array[cur_right], pivot):
            cur_right -= 1
        if cur_left >= cur_right:
            break

        array[cur_left], array[cur_right] = array[cur_right], array[cur_left]
        cur_left += 1
        cur_right -= 1

    return cur_right


def is_score_better(student_1, student_2, name_key=0, tasks_key=1, penalty_key=2):
    if student_1[tasks_key] > student_2[tasks_key]:
        return True
    elif student_1[tasks_key] < student_2[tasks_key]:
        return False
    else:
        if student_1[penalty_key] < student_2[penalty_key]:
            return True
        elif student_1[penalty_key] > student_2[penalty_key]:
            return False
        else:
            return student_1[name_key] < student_2[name_key]


def print_rating(students_score_list, name_key=0):
    for student_score in students_score_list[::-1]:
        print(student_score[name_key])


def get_students_score_list(tasks_key=1, penalty_key=2):
    students_count = int(sys.stdin.readline())
    students_score_list = []

    for i in range(students_count):
        student_score = sys.stdin.readline().strip().split(' ')
        student_score[tasks_key] = int(student_score[tasks_key])
        student_score[penalty_key] = int(student_score[penalty_key])
        students_score_list.append(student_score)

    return students_score_list


def main():
    students_score_list = get_students_score_list()
    sort(students_score_list, is_score_better)
    print_rating(students_score_list)


if __name__ == '__main__':
    main()


