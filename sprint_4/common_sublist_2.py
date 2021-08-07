import sys


def max_sublist_len(a, b):
    a_len = len(a)
    b_len = len(b)
    matrix = [[0 for x in range(b_len)] for y in range(a_len)]

    max_value = 0

    for i in range(a_len):
        for j in range(b_len):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1

                if matrix[i][j] > max_value:
                    max_value = matrix[i][j]

    return max_value


def main():
    sys.stdin.readline().strip()
    a = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    sys.stdin.readline().strip()
    b = [int(i) for i in sys.stdin.readline().strip().split(' ')]

    print(max_sublist_len(a, b))


if __name__ == '__main__':
    main()
