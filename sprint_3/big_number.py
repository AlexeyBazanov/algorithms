import sys


def is_first_number_less(number_1, number_2):
    n1 = str(number_1) + str(number_2)
    n2 = str(number_2) + str(number_1)
    return int(n1) < int(n2)


def insert_sort(data, less):
    for i in range(1, len(data)):
        j = i - 1
        key = data[i]

        while j >= 0 and less(data[j], key):
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


def main():
    sys.stdin.readline()
    numbers = sys.stdin.readline().strip().split(' ')
    numbers = [int(i) for i in numbers]
    sorted_numbers = insert_sort(numbers, is_first_number_less)
    print(''.join(map(str, sorted_numbers)))


main()

