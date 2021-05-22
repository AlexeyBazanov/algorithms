# ID посылки - 48218763
import sys


def get_numbers_counter_map(numbers):
    numbers_counter_map = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '.': 0
    }

    for number in numbers:
        numbers_counter_map[number] += 1

    numbers_counter_map.pop('.', None)

    return numbers_counter_map


def collect_numbers(numbers_row1, numbers_row2, numbers_row3, numbers_row4):
    numbers = []

    for number in numbers_row1+numbers_row2+numbers_row3+numbers_row4:
        numbers.append(number)

    return numbers


def count_points(numbers_counter_map, presses_per_time):
    points = 0

    for number in numbers_counter_map:
        if 0 < numbers_counter_map[number] <= presses_per_time:
            points += 1

    return points


def get_result_of_simulator(numbers_row1, numbers_row2, numbers_row3, numbers_row4, presses_per_time):
    numbers = collect_numbers(numbers_row1, numbers_row2, numbers_row3, numbers_row4)

    numbers_counter_map = get_numbers_counter_map(numbers)

    return count_points(numbers_counter_map, presses_per_time)


def main():
    presses_per_time = int(sys.stdin.readline().strip()) * 2

    numbers_row1 = sys.stdin.readline().strip()
    numbers_row2 = sys.stdin.readline().strip()
    numbers_row3 = sys.stdin.readline().strip()
    numbers_row4 = sys.stdin.readline().strip()

    points = get_result_of_simulator(
        numbers_row1, numbers_row2,
        numbers_row3, numbers_row4,
        presses_per_time
    )

    print(str(points))


main()
