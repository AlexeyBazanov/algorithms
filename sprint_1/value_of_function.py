import sys


def main():
    a, x, b, c = sys.stdin.readline().strip().split()
    return (int(a) * int(x) * int(x)) + (int(b) * int(x)) + int(c)


print(main())
