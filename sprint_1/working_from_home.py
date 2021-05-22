import sys


def decimal_to_binary(decimal):
    binary_digits = ''

    while int(decimal / 2) >= 1:
        binary_digits += str(decimal % 2)
        decimal = int(decimal / 2)

    binary_digits += str(decimal)

    return binary_digits[::-1]


def main():
    decimal = int(sys.stdin.readline().strip())
    print(decimal_to_binary(decimal))


main()
