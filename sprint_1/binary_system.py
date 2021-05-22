import sys


def add_leading_zeros(number, zeros_num):
    for i in range(zeros_num):
        number = '0' + number
    return number


def sum_two_digits(digit_one, digit_two):
    if digit_one == '1' and digit_two == '1':
        return ['1', '0']
    elif (digit_one == '1' and digit_two == '0') or (digit_one == '0' and digit_two == '1'):
        return ['0', '1']
    else:
        return ['0', '0']


def sum_two_numbers(number_one, number_two):
    number_one_len = len(number_one)
    number_two_len = len(number_two)
    len_diff = abs(number_one_len - number_two_len)

    if number_one_len < number_two_len:
        number_one = add_leading_zeros(number_one, len_diff)
    else:
        number_two = add_leading_zeros(number_two, len_diff)

    number_one = number_one[::-1]
    number_two = number_two[::-1]

    numbers_sum = ''
    carry = '0'

    for i in range(len(number_one)):
        current_sum = sum_two_digits(number_one[i], number_two[i])
        current_carry = current_sum[0]

        if carry == '1':
            current_sum = sum_two_digits(current_sum[1], carry)

        if current_sum[0] == '1':
            current_carry = '1'

        carry = current_carry

        numbers_sum = current_sum[1] + numbers_sum

    if carry == '1':
        numbers_sum = carry + numbers_sum

    return numbers_sum


def main():
    number_one = sys.stdin.readline().strip()
    number_two = sys.stdin.readline().strip()
    print(sum_two_numbers(number_one, number_two))


main()
