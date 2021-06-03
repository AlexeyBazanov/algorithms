import sys


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





