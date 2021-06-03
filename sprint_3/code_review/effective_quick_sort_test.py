import unittest
import effective_quick_sort


class EffectiveQuickSortTest(unittest.TestCase):

    def test_sort(self):
        array = [2, 3, 1, 4, 6]
        effective_quick_sort.sort(array)
        self.assertEqual(array, [1, 2, 3, 4, 6])

    def test_key(self):
        student_score_1 = ['John', 4, 100]
        student_score_2 = ['Mike', 2, 40]
        self.assertEqual(effective_quick_sort.is_score_better(student_score_1, student_score_2), True)

        student_score_2 = ['Mike', 4, 50]
        self.assertEqual(effective_quick_sort.is_score_better(student_score_1, student_score_2), False)

        student_score_2 = ['Alex', 4, 100]
        self.assertEqual(effective_quick_sort.is_score_better(student_score_1, student_score_2), False)

    def test_sort_with_key(self):
        student_scores = [
            ['John', 4, 100],
            ['Mike', 2, 40],
            ['Kate', 3, 50],
            ['Alex', 4, 100],
            ['Lisa', 6, 10]
        ]
        effective_quick_sort.sort(student_scores, effective_quick_sort.is_score_better)
        self.assertEqual(student_scores, [
            ['Mike', 2, 40],
            ['Kate', 3, 50],
            ['John', 4, 100],
            ['Alex', 4, 100],
            ['Lisa', 6, 10]
        ])


if __name__ == '__main__':
    unittest.main()
