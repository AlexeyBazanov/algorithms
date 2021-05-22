import sys


def search(item, array):

    # [3, 4, 5, 6, 1, 2]

    mid = len(array) // 2

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == item:
            return mid
        elif array[left] < array[mid] and array[left] <= item <= array[mid]:
            pass


    # if array[mid] > array[0]:

    for i in range(len(array)):
        if array[i] == item:
            return i
    return -1


def binary_search(number, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if number < array[mid]:
            right = mid - 1
        elif number > array[mid]:
            left = mid + 1
        else:
            return mid

    return -1


