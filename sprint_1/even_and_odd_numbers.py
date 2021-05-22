import sys


def is_win():
    num1, num2, num3 = sys.stdin.readline().strip().split()
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    return (num1 % 2 == 0) == (num2 % 2 == 0) == (num3 % 2 == 0)


def print_result():
    print("WIN" if is_win() else "FAIL")


print_result()
