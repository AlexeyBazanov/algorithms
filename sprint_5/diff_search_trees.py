import sys


def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def tbs_numbers(n):
    return int(factorial(2 * n) / (factorial(n + 1) * factorial(n)))


def main():
    n = int(sys.stdin.readline().strip())
    print(tbs_numbers(n))


if __name__ == '__main__':
    main()
