import unittest

from kata_5kyu.valid_parentheses import valid_parentheses


class TestValidParentheses(unittest.TestCase):
    def test_simple_true_base_case(self):
        test_input = "()"

        actual = valid_parentheses(test_input)

        self.assertEqual(True, actual)

    def test_simple_false_base_case(self):
        test_input = "("

        actual = valid_parentheses(test_input)

        self.assertEqual(False, actual)

    def test_true_with_empty_string(self):
        test_input = ""

        actual = valid_parentheses(test_input)

        self.assertEqual(True, actual)

    def test_false_with_with_no_parentheses(self):
        test_input = "abc"

        actual = valid_parentheses(test_input)

        self.assertEqual(True, actual)

    def test_true_with_multiple_parentheses(self):
        test_input = "(())((()())())"

        actual = valid_parentheses(test_input)

        self.assertEqual(True, actual)

    def test_false_with_multiple_parentheses(self):
        test_input = ")(()))"

        actual = valid_parentheses(test_input)

        self.assertEqual(False, actual)

    def test_true_with_other_characters(self):
        test_input = "(())(sdfgdfh(()())()74er')"

        actual = valid_parentheses(test_input)

        self.assertEqual(True, actual)

    def test_true_with_other_forms_of_brackets(self):
        test_input = "(({))((()())(]))"

        actual = valid_parentheses(test_input)

        self.assertEqual(True, actual)

    def test_false_with_other_characters(self):
        test_input = "(())((sdfgdfh(()())()74er')"

        actual = valid_parentheses(test_input)

        self.assertEqual(False, actual)

    def test_false_with_other_forms_of_brackets(self):
        test_input = "(({))(((()())(]))"

        actual = valid_parentheses(test_input)

        self.assertEqual(False, actual)

    def test_true_with_spaces(self):
        test_input = "(    )"

        actual = valid_parentheses(test_input)

        self.assertEqual(True, actual)

    def test_false_with_spaces(self):
        test_input = "    )"

        actual = valid_parentheses(test_input)

        self.assertEqual(False, actual)
