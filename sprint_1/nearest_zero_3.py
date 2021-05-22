# ID посылки - 48219003
import sys


def find_positions_distance(position_one, position_two):
    return abs((position_one + 1) - (position_two + 1))


def get_positions_range(sequence_len, reverse):
    if reverse:
        return range(sequence_len - 1, -1, -1)
    else:
        return range(sequence_len)


def find_nearest_zero_distances_by_direction(distances, sequence, sequence_len, reverse=False, undefined_distance=-1, zero='0'):
    last_zero_position = None

    positions = get_positions_range(sequence_len, reverse)

    for position in positions:
        if sequence[position] == zero:
            distances[position] = 0
            last_zero_position = position
        else:
            if last_zero_position is None:
                continue
            else:
                distance = find_positions_distance(position, last_zero_position)

                if distances[position] == undefined_distance:
                    distances[position] = distance
                elif distance < distances[position]:
                    distances[position] = distance

    return distances


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


main()
