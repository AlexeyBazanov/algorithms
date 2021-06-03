import sys


def search(needle, numbers):
    return broken_search(numbers, needle, 0, len(numbers) - 1)


def broken_search(numbers, needle, left, right):
    mid = (left + right) // 2

    if needle == numbers[mid]:
        return mid

    if right < left:
        return -1

    if numbers[left] < numbers[mid]:
        if numbers[left] <= needle < numbers[mid]:
            return broken_search(numbers, needle, left, mid - 1)
        else:
            return broken_search(numbers, needle, mid + 1, right)
    elif numbers[left] > numbers[mid]:
        if numbers[mid] < needle <= numbers[right]:
            return broken_search(numbers, needle, mid + 1, right)
        else:
            return broken_search(numbers, needle, left, mid - 1)
    else:
        if numbers[mid] != numbers[right]:
            return broken_search(numbers, needle, mid + 1, right)
        else:
            result = broken_search(numbers, needle, left, mid - 1)

            if result == -1:
                return broken_search(numbers, needle, mid + 1, right)
            else:
                return result


def main():
    sys.stdin.readline()
    needle = int(sys.stdin.readline().strip())
    numbers = sys.stdin.readline().strip().split(' ')
    numbers = [int(i) for i in numbers]
    print(search(needle, numbers))


if __name__ == '__main__':
    main()
