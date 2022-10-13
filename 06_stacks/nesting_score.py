def nesting_score(string):
    stack = [0]

    for s in string:
        if s == '[':
            stack.append(0)
        else:
            popped = stack.pop()
            if popped == 0:
                stack[-1] += 1
            else:
                stack[-1] += 2 * popped

    return stack[0]
