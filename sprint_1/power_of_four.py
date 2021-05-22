import sys
import math


def is_power(a, b):
    log = math.log(a, b)
    return int(log) == log


def main():
    number = int(sys.stdin.readline().strip())
    print('True' if is_power(number, 4) else 'False')


main()
