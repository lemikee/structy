import math


def _summing_squares(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    min_squares = float('inf')

    for i in range(1, math.floor(math.sqrt(n) + 1)):
        square = i * i
        attempt = _summing_squares(n - square, memo)
        min_squares = min(min_squares, attempt + 1)

    memo[n] = min_squares
    return memo[n]


def summing_squares(n):
    memo = {}
    return _summing_squares(n, memo)
