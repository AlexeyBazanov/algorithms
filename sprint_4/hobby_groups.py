import sys

unique_values = {}


def print_unique(value):
    if value not in unique_values:
        print(value)
        unique_values[value] = 1


if __name__ == '__main__':
    hobby_list_len = int(sys.stdin.readline().strip())

    for i in range(hobby_list_len):
        print_unique(sys.stdin.readline().strip())
