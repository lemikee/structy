def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]
    if s == '':
        return True

    for word in words:
        if s.startswith(word):
            remainder = s[len(word):]
            if _can_concat(remainder, words, memo):
                memo[s] = True
                return True

    memo[s] = False
    return False


def can_concat(s, words):
    memo = {}
    return _can_concat(s, words, memo)
