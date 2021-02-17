import unittest

from problem1 import disemvowel


class TestKata1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")


if __name__ == '__main__':
    unittest.main()
