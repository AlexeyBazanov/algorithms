import sys


def eratosthenes_sieve(n):
    sieve = [0] * n
    i = 2

    while i*i < n:
        if sieve[i] == 0:
            k = i*i
            while k < n:
                sieve[k] = 1
                k += i
        i += 1

    return sieve


def prime_numbers(n):
    numbers = []
    sieve = eratosthenes_sieve(n)

    for i in range(2, len(sieve)):
        if sieve[i] == 0:
            numbers.append(i)

    return numbers


def factorization(n):
    divisors = []
    prime_matrix = prime_numbers(100)

    while n > 1:
        for p in prime_matrix:
            if n % p == 0:
                divisors.append(p)
                n = n / p
                break

    return divisors


def main():
    n = int(sys.stdin.readline().strip())
    divisors = factorization(n)
    divisors.sort()
    print(' '.join(map(str, divisors)))


main()


