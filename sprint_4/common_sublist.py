import random
import sys


def max_sublist_len(a, b):
    a_len = len(a)
    b_len = len(b)

    if a_len == 0 or b_len == 0:
        return 0

    max_len, cur_len, row = 0, 0, 0
    col = a_len - 1

    while row < b_len:
        i, j = row, col
        cur_len = 0

        while i < b_len and j < a_len:
            if b[i] == a[j]:
                cur_len += 1
            else:
                cur_len = 0

            if cur_len > max_len:
                max_len = cur_len

            i += 1
            j += 1

        if col > 0:
            col -= 1
        else:
            row += 1

    return max_len


def main():
    sys.stdin.readline().strip()
    a = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    sys.stdin.readline().strip()
    b = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    print(max_sublist_len(a, b))


if __name__ == '__main__':
    # main()

    a = [random.randint(0, 255)] * 10000
    b = [random.randint(0, 255)] * 10000

    print(max_sublist_len(a, b))
