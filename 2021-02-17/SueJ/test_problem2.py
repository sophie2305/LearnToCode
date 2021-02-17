import unittest

from problem2 import validate_pin


class TestKata1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(validate_pin("1234"), True)

    def test_2(self):
        self.assertEqual(validate_pin("090909"), True)

    def test_3(self):
        self.assertEqual(validate_pin("1234567"), False)

    def test_4(self):
        self.assertEqual(validate_pin("a234"), False)

    def test_5(self):
        self.assertEqual(validate_pin("-1234"), False)


if __name__ == '__main__':
    unittest.main()
