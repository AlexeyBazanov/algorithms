import sys


def collect_zeros_positions(sequence, sequence_len):
    zeros_positions = []

    for i in range(sequence_len):
        if sequence[i] == '0':
            zeros_positions.append(i)

    return zeros_positions


def find_positions_distance(position_one, position_two):
    return abs((position_one + 1) - (position_two + 1))


def split_list(full_list):
    half = len(full_list) // 2
    return full_list[:half], full_list[half:]


def find_nearest_zero_distance(original_pos, zeros_positions):
    while len(zeros_positions) > 1:
        left_zeros_positions, right_zeros_positions = split_list(zeros_positions)
        left_position_distance = find_positions_distance(original_pos, left_zeros_positions[-1])
        right_position_distance = find_positions_distance(original_pos, right_zeros_positions[0])

        if left_position_distance < right_position_distance:
            zeros_positions = left_zeros_positions
        else:
            zeros_positions = right_zeros_positions

    return find_positions_distance(original_pos, zeros_positions[0])


def find_all_nearest_zero_distances(sequence, sequence_len, zeros_positions):
    result = ''

    for i in range(sequence_len):
        if sequence[i] == '0':
            result += '0'
        else:
            result += str(find_nearest_zero_distance(i, zeros_positions))

        if i < sequence_len - 1:
            result += ' '

    return result


def nearest_zeros():
    sequence_len = int(sys.stdin.readline().strip())
    sequence = sys.stdin.readline().strip().split()
    zeros_positions = collect_zeros_positions(sequence, sequence_len)
    return find_all_nearest_zero_distances(sequence, sequence_len, zeros_positions)


def test_collect_zeros_positions():
    sequence = ['1', '0']
    sequence_len = 2
    assert collect_zeros_positions(sequence, sequence_len) == [1], "Should be [1]"

    sequence = ['0', '1', '2', '0', '3', '0', '4']
    sequence_len = 7
    assert collect_zeros_positions(sequence, sequence_len) == [0, 3, 5], "Should be [0, 3, 5]"


def test_find_positions_distance():
    assert find_positions_distance(1, 5) == 4, "Should be 4"
    assert find_positions_distance(7, 2) == 5, "Should be 5"
    assert find_positions_distance(0, 8) == 8, "Should be 8"


def test_find_nearest_zero_distance():
    assert find_nearest_zero_distance(1, [2]) == 1, "Should be 1"
    assert find_nearest_zero_distance(1, [4, 9, 15]) == 3, "Should be 3"
    assert find_nearest_zero_distance(10, [1, 5, 25]) == 5, "Should be 5"
    assert find_nearest_zero_distance(55, [25, 40, 100]) == 15, "Should be 15"


def test_find_all_nearest_zero_distances():
    assert find_all_nearest_zero_distances([0, 1, 4, 9, 0], 5, [0, 4]) == '0 1 2 1 0', "Should be '0 1 2 1 0'"
    assert find_all_nearest_zero_distances([0, 7, 9, 4, 8, 20], 6, [0]) == '0 1 2 3 4 5', "Should be '0 1 2 3 4 5'"


def main():
    if __name__ == "__main__":
        test_collect_zeros_positions()
        test_find_positions_distance()
        test_find_nearest_zero_distance()
        test_find_all_nearest_zero_distances()

    print(nearest_zeros())


main()
