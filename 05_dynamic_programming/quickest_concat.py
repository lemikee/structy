def _quickest_concat(s, words, memo):
    if s in memo:
        return memo[s]
    if s == '':
        return 0

    min_words = float('inf')
    for word in words:
        if s.startswith(word):
            remainder = s[len(word):]
            attempt = 1 + _quickest_concat(remainder, words, memo)
            min_words = min(min_words, attempt)

    memo[s] = min_words
    return min_words


def quickest_concat(s, words):
    memo = {}
    result = _quickest_concat(s, words, memo)

    if result == float('inf'):
        return -1
    else:
        return result
