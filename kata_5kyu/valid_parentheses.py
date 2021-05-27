def valid_parentheses(string):
    paren_stack = []

    for char in string:
        if char == "(":
            paren_stack.append(char)
        if char == ")":
            try:
                if paren_stack[-1] == "(":
                    paren_stack.pop()
            except IndexError:
                return False

    return len(paren_stack) == 0
