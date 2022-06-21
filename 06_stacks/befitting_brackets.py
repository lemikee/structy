def befitting_brackets(string):
    stack = []

    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for s in string:
        if s in brackets:
            stack.append(brackets[s])
        # elif len(stack) == 0:
        #   return False
        # elif stack[-1] == s:
        #   stack.pop()
        # else:
        #   return False
        else:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                # stack is empty (nothing to match with ie just opening brackets) or not well formed
                return False

    return len(stack) == 0

#   if we see opening bracket, put matching closing bracket in our stack
#   if we have closing bracket, and matching closing bracket at top of our stack
#     then we know that we have a well formed set of brackets
