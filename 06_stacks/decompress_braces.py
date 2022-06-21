def decompress_braces(string):
    stack = []

    for s in string:
        if s.isdigit():
            stack.append(int(s))
        else:
            if s == '}':
                segment = ''

                while isinstance(stack[-1], str):
                    popped = stack.pop()
                    segment = popped + segment
                num = stack.pop()
                stack.append(segment * num)
            elif s != '{':
                stack.append(s)

    return ''.join(stack)
