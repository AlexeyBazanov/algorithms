import sys


class NearestZeroFinder:

    def __init__(self, sequence, sequence_len, undefined_distance=-1, zero_sign='0'):
        self.sequence = sequence
        self.sequence_len = sequence_len
        self.undefined_distance = undefined_distance
        self.zero_sign = zero_sign
        self.distances = None

    def print_distances(self):
        if self.distances is None:
            print('Distances not calculated yet.')
        else:
            print(' '.join(map(str, self.distances)))

    def calculate_distances(self):
        self.__clear_distances()
        self.__find_nearest_zero_distances()
        self.__find_nearest_zero_distances(True)

    def __find_nearest_zero_distances(self, reverse=False):
        positions = self.__get_positions_range(reverse)
        last_zero_position = None

        for position in positions:
            if self.sequence[position] == self.zero_sign:
                self.distances[position] = 0
                last_zero_position = position
            else:
                if last_zero_position is None:
                    continue
                else:
                    self.__set_distance(position, last_zero_position)

    def __set_distance(self, position, zero_position):
        distance = self.__find_positions_distance(position, zero_position)

        if self.distances[position] == self.undefined_distance:
            self.distances[position] = distance
        elif distance < self.distances[position]:
            self.distances[position] = distance

    def __get_positions_range(self, reverse=False):
        if reverse:
            return range(self.sequence_len - 1, -1, -1)
        else:
            return range(self.sequence_len)

    def __find_positions_distance(self, position_one, position_two):
        return abs((position_one + 1) - (position_two + 1))

    def __clear_distances(self):
        self.distances = [self.undefined_distance] * self.sequence_len


def main():
    sequence_len = int(sys.stdin.readline().strip())
    sequence = sys.stdin.readline().strip().split()

    nearest_zero_finder = NearestZeroFinder(sequence, sequence_len)

    nearest_zero_finder.calculate_distances()
    nearest_zero_finder.print_distances()


if __name__ == '__main__':
    main()


