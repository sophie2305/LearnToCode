import unittest
from parameterized import parameterized
from kata_5kyu.greed_is_good import greed_is_good_score


class TestGreedIsGood(unittest.TestCase):
    def test_zero_case(self):
        dice = [2, 3, 4, 6, 2]

        actual = greed_is_good_score(dice)
        self.assertEqual(0, actual)

    @parameterized.expand([
        ([1, 1, 1, 3, 3], 1000),
        ([2, 2, 2, 3, 3], 200),
        ([3, 3, 3, 3, 3], 300),
        ([4, 4, 4, 3, 3], 400),
        ([5, 5, 5, 3, 3], 500),
        ([6, 6, 6, 3, 3], 600),
        ([1, 2, 3, 4, 6], 100),
        ([5, 2, 3, 4, 6], 50),
    ])
    def test_single_score_cases(self, dice, expected):
        actual = greed_is_good_score(dice)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ([1, 1, 1, 1, 1], 1200),
        ([1, 1, 1, 1, 3], 1100),
        ([1, 1, 1, 5, 5], 1100),
        ([1, 1, 1, 5, 3], 1050),
        ([1, 1, 1, 1, 5], 1150),
        ([2, 4, 4, 5, 4], 450),
        ([3, 4, 5, 3, 3], 350),
        ([1, 5, 1, 3, 4], 250),
    ])
    def test_mixed_score_cases(self, dice, expected):
        actual = greed_is_good_score(dice)
        self.assertEqual(expected, actual)
