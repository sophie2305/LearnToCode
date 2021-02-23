import unittest

from parameterized import parameterized

from solutions import disemvowel, validate_pin, to_camel_case, validate_password


class TestSolutions(unittest.TestCase):
    @parameterized.expand([
        ('This website is for losers LOL!', 'Ths wbst s fr lsrs LL!'),
        ('No offense but,\nYour writing is among the worst I\'ve ever read',
         'N ffns bt,\nYr wrtng s mng th wrst \'v vr rd'),
        ('What are you, a communist?', 'Wht r y,  cmmnst?')
    ])
    def test_disemvowel(self, string, expected):
        actual = disemvowel(string)

        self.assertEqual(actual, expected)

    @parameterized.expand([
        ('0123', True),
        ('012345', True),
        ('a235', False),
        ('1.234', False)

    ])
    def test_validate_pin(self, pin, expected):
        actual = validate_pin(pin)

        self.assertEqual(actual, expected)

    @parameterized.expand([
        ('', ''),
        ('the_stealth_warrior', 'theStealthWarrior'),
        ('The-Stealth-Warrior', 'TheStealthWarrior'),
        ('A-B-C', 'ABC')

    ])
    def test_to_camel_case(self, text, expected):
        actual = to_camel_case(text)

        self.assertEqual(actual, expected)

    @parameterized.expand([
        ('fjd3IR9', True),
        ('Password123', True),
        ('ghdfj32', False),
        ('DSJKHD23', False),
        ('dsF43', False),
        ('fjd3IR9.;', False),
        ('fjd3  IR9', False)

    ])
    def test_validate_password(self, password, expected):
        actual = validate_password(password)

        self.assertEqual(actual, expected)
