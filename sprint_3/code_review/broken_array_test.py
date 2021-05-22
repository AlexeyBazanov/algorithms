import unittest
import broken_array


class BrokenArrayTest(unittest.TestCase):

    def test_search(self):
        array = [2, 3, 1]
        self.assertEqual(broken_array.search(2, array), 0)
        self.assertEqual(broken_array.search(3, array), 1)
        self.assertEqual(broken_array.search(1, array), 2)
        self.assertEqual(broken_array.search(4, array), -1)

    def test_binary_search(self):
        array = [1, 2, 3]
        self.assertEqual(broken_array.binary_search(1, array), 0)
        self.assertEqual(broken_array.binary_search(2, array), 1)
        self.assertEqual(broken_array.binary_search(3, array), 2)
        self.assertEqual(broken_array.binary_search(4, array), -1)


if __name__ == '__main__':
    unittest.main()
