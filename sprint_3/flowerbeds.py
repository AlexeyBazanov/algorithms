import sys


def merge_sort(array, key):
    array_len = len(array)

    if array_len == 1:
        return array

    left = merge_sort(array[:array_len // 2], key)
    right = merge_sort(array[array_len // 2:], key)

    result = [None] * array_len

    left_len = len(left)
    right_len = len(right)

    left_idx, right_idx, current_idx = 0, 0, 0

    while left_idx < left_len and right_idx < right_len:
        if key(left[left_idx]) <= key(right[right_idx]):
            result[current_idx] = left[left_idx]
            left_idx += 1
        else:
            result[current_idx] = right[right_idx]
            right_idx += 1
        current_idx += 1

    while left_idx < left_len:
        result[current_idx] = left[left_idx]
        left_idx += 1
        current_idx += 1

    while right_idx < right_len:
        result[current_idx] = right[right_idx]
        right_idx += 1
        current_idx += 1

    return result


def merge_intervals(intervals):
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        x1 = intervals[i][0]
        y1 = intervals[i][1]
        y2 = result[len(result) - 1][1]

        if y2 >= x1:
            result[len(result) - 1][1] = max(y1, y2)
        else:
            result.append(intervals[i])

    return result


def main():
    intervals_count = int(sys.stdin.readline().strip())
    intervals = []

    for i in range(intervals_count):
        interval = sys.stdin.readline().strip().split(' ')
        interval = list(map(int, interval))
        intervals.append(interval)

    merged_intervals = merge_intervals(sorted(intervals, key=lambda x: x[0]))

    for i in range(len(merged_intervals)):
        print("{0} {1}".format(merged_intervals[i][0], merged_intervals[i][1]))


main()
