import unittest
import polynomial_hash


class ContestTest(unittest.TestCase):
    def test_get_hash(self):
        self.assertEqual(polynomial_hash.get_hash('a', 123, 100003), 97)
        self.assertEqual(polynomial_hash.get_hash('hash', 123, 100003), 6080)
        self.assertEqual(polynomial_hash.get_hash('HaSH', 123, 100003), 56156)


if __name__ == '__main__':
    unittest.main()
