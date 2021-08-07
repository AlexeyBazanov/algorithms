import sys


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and is_first_student_better(arr[i], arr[l]):
        largest = l

    if r < n and is_first_student_better(arr[largest], arr[r]):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def is_first_student_better(student1, student2, name_key=0, tasks_key=1, penalty_key=2):
    if student1[tasks_key] == student2[tasks_key]:
        if student1[penalty_key] == student2[penalty_key]:
            return student1[name_key] < student2[name_key]
        return student1[penalty_key] < student2[penalty_key]
    return student1[tasks_key] > student2[tasks_key]


def print_score(name_key=0, tasks_key=1, penalty_key=2):
    students_number = int(sys.stdin.readline().strip())
    heap = []

    for i in range(students_number):
        student_score = sys.stdin.readline().strip().split(' ')
        student_score[tasks_key] = int(student_score[tasks_key])
        student_score[penalty_key] = int(student_score[penalty_key])
        heap.append(student_score)

    heapSort(heap)

    for i in range(students_number):
        print(heap[i][name_key])


if __name__ == '__main__':
    print_score()