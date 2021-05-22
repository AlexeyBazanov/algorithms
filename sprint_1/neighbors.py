import sys


def get_neighbors_nums():
    row_num = int(sys.stdin.readline().strip())
    col_num = int(sys.stdin.readline().strip())
    matrix = []
    neighbors_nums = []

    for i in range(row_num):
        matrix.append(sys.stdin.readline().strip().split())

    y_pos = int(sys.stdin.readline().strip())
    x_pos = int(sys.stdin.readline().strip())

    next_x = x_pos + 1
    prev_x = x_pos - 1
    next_y = y_pos + 1
    prev_y = y_pos - 1

    if next_x < col_num:
        neighbors_nums.append(int(matrix[y_pos][next_x]))
    if prev_x > -1:
        neighbors_nums.append(int(matrix[y_pos][prev_x]))
    if next_y < row_num:
        neighbors_nums.append(int(matrix[next_y][x_pos]))
    if prev_y > -1:
        neighbors_nums.append(int(matrix[prev_y][x_pos]))

    return neighbors_nums


def print_result(nums):
    nums.sort()
    nums = map(str, nums)
    print(' '.join(nums))


print_result(get_neighbors_nums())
