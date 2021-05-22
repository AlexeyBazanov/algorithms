# ID посылки - 48219003
import sys


def find_positions_distance(position_one, position_two):
    return abs(position_one - position_two)


def get_positions_range(sequence_len, reverse):
    if reverse:
        return range(sequence_len - 1, -1, -1)
    else:
        return range(sequence_len)


def enumerate_sequence(sequence, reverse):
    if reverse:
        return enumerate(reversed(sequence))
    else:
        return enumerate(sequence)


def find_nearest_zero_distances_by_direction(distances, sequence, sequence_len, reverse=False, undefined_distance=-1, zero='0'):
    last_zero_position = None

    for position in get_positions_range(sequence_len, reverse):
        if sequence[position] == zero:
            distances[position] = 0
            last_zero_position = position
        else:
            if last_zero_position is None:
                continue

            distances[position] = find_distance_for_position(
                distances[position],
                position,
                last_zero_position,
                undefined_distance
            )

    return distances


def find_distance_for_position(last_distance, position, zero_position, undefined_distance=-1):
    new_distance = find_positions_distance(position, zero_position)

    if last_distance == undefined_distance:
        return new_distance
    else:
        return min(last_distance, new_distance)


def find_nearest_zero_distances(sequence, sequence_len, undefined_distance=-1):
    distances = [undefined_distance] * sequence_len

    distances = find_nearest_zero_distances_by_direction(distances, sequence, sequence_len)
    distances = find_nearest_zero_distances_by_direction(distances, sequence, sequence_len, True)

    return distances


def print_distances(distances):
    print(' '.join(map(str, distances)))


def main():
    sequence_len = int(sys.stdin.readline().strip())
    sequence = sys.stdin.readline().strip().split()

    distances = find_nearest_zero_distances(sequence, sequence_len)

    print_distances(distances)


if __name__ == "__main__":
    main()
