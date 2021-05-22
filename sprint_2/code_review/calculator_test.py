import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.calculate('2 2 +')
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = self.calculator.calculate('6 2 -')
        self.assertEqual(result, 4)

    def test_multiplication(self):
        result = self.calculator.calculate('2 2 *')
        self.assertEqual(result, 4)

    def test_division(self):
        result = self.calculator.calculate('8 2 /')
        self.assertEqual(result, 4)

    def test_mixed_expression(self):
        result = self.calculator.calculate('8 2 / 2 * 8 - 4 +')
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        result = self.calculator.calculate('-2 6 +')
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        result = self.calculator.calculate('4 0 /')
        self.assertEqual(result, None)

    def test_incorrect_expression(self):
        result = self.calculator.calculate('foo bar 0 +')
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
