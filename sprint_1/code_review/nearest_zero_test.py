import unittest
from nearest_zero import NearestZeroFinder


class TestNearestZeroFinder(unittest.TestCase):

    def test_calculate_distances(self):
        sequence = ['0', '1', '4', '9', '0']
        sequence_len = 5

        nearest_zero_finder = NearestZeroFinder(sequence, sequence_len)
        nearest_zero_finder.calculate_distances()

        self.assertEqual(nearest_zero_finder.distances, [0, 1, 2, 1, 0])

        nearest_zero_finder.sequence = ['0', '7', '9', '4', '8', '20']
        nearest_zero_finder.sequence_len = 6
        nearest_zero_finder.calculate_distances()

        self.assertEqual(nearest_zero_finder.distances, [0, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
