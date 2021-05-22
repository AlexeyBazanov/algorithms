import sys


def main():
    nums_of_digits = int(sys.stdin.readline().strip())
    digits = sys.stdin.readline().strip().split()
    digits = list(map(int, digits))
    days = []

    if len(digits) < 2:
        return 1

    if digits[0] > digits[1]:
        days.append(digits[0])

    if digits[-1] > digits[-2]:
        days.append(digits[-1])

    for i in range(1, nums_of_digits - 1):
        if digits[i] > digits[i - 1] and digits[i] > digits[i + 1]:
            days.append(digits[i])

    return len(days)


print(main())
