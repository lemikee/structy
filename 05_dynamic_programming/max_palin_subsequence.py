def _max_palin_subsequence(string, i, j, memo):
    key = str(i) + ',' + str(j)
    if key in memo:
        return memo[key]

    if i > j:
        return 0
    if i == j:
        return 1

    if string[i] == string[j]:
        memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
        # return 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
    else:
        memo[key] = max(
            _max_palin_subsequence(string, i + 1, j, memo),
            _max_palin_subsequence(string, i, j - 1, memo)
        )

    return memo[key]


def max_palin_subsequence(string):
    memo = {}
    return _max_palin_subsequence(string, 0, len(string) - 1, memo)
