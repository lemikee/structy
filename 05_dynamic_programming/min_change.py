def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    min_coins = float('inf')

    for coin in coins:
        attempt = _min_change(amount - coin, coins, memo)
        min_coins = min(min_coins, attempt + 1)

    memo[amount] = min_coins
    return min_coins


def min_change(amount, coins):
    memo = {}

    result = _min_change(amount, coins, memo)

    if result == float('inf'):
        return -1
    else:
        return result
