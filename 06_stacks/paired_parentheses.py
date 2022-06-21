def paired_parentheses(string):
    stack = []

    for s in string:
        if s == '(':
            stack.append(')')
        elif s == ')':
            if stack and stack[-1] == s:
                stack.pop()
            else:
                return False

    return len(stack) == 0
