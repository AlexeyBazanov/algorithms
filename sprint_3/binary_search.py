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
