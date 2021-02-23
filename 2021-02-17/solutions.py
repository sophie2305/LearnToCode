import re


# Problem 1
def disemvowel(string):
    return re.sub('[aeiouAEIOU]', '', string)


# Problem 2
def validate_pin(pin):
    return bool(re.fullmatch(r'(\d{4}|\d{6})', pin))


# Problem 3
def to_camel_case(text):
    # original solution
    return ''.join(word if i == 0 else word.capitalize() for i, word in enumerate(re.split("[-_]", text)))
    # like this solution
    # return sub("[-_](.)",lambda x: x.group(1).upper(),text)


# Bonus Problem
def validate_password(password):
    # ooo lookahead assertions 0.0
    return bool(re.search('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,}$', password))
