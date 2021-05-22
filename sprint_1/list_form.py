import sys


def str_to_int(string):
    result = ''

    for char in string:
        if char != ' ':
            result += char

    return int(result)


def list_form(n, k):
    summa = str(str_to_int(n) + str_to_int(k))
    result = ''

    for i in range(len(summa)):
        if i > 0:
            result += ' '+summa[i]
        else:
            result += summa[i]

    return result


def main():
    sys.stdin.readline()
    number_one = sys.stdin.readline().strip()
    number_two = sys.stdin.readline().strip()
    print(list_form(number_one, number_two))


main()
