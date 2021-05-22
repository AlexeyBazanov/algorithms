import sys


def factorization(n):
    result = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            result.append(divisor)
            n //= divisor
        else:
            divisor += 1
    if n > 1:
        result.append(n)
    return result


def main():
    n = int(sys.stdin.readline().strip())
    divisors = factorization(n)
    print(' '.join(map(str, divisors)))


main()
