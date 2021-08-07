import unittest
import contest


class ContestTest(unittest.TestCase):

    def test_sequence(self):
        contest_result = [0, 1, 0]
        self.assertEqual(contest.max_draw_sequence(contest_result), 2)

        contest_result = [0, 1, 1, 0, 1, 0]
        self.assertEqual(contest.max_draw_sequence(contest_result), 6)

        contest_result = [0, 0]
        self.assertEqual(contest.max_draw_sequence(contest_result), 0)

        contest_result = [0, 1]
        self.assertEqual(contest.max_draw_sequence(contest_result), 2)


if __name__ == '__main__':
    unittest.main()
