import sys


def print_array(array):
    print(' '.join(map(str, array)))


def bubble_sort(array):
    array_len = len(array)
    replaces = 1
    offset = 0

    while replaces > 0:
        replaces = 0

        for i in range(array_len - offset - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                replaces += 1

        offset += 1

        if replaces > 0:
            print_array(array)

        if offset == 1 and replaces == 0:
            print_array(array)

    return array


def main():
    sys.stdin.readline()
    array = sys.stdin.readline().strip().split(' ')
    array = [int(i) for i in array]
    bubble_sort(array)


main()
