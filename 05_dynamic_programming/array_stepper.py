def _array_stepper(numbers, i, memo):
    if i in memo:
        return memo[i]
    if i >= len(numbers):
        return True
    if i == len(numbers) - 1:
        return True

    possible_steps = numbers[i]

    for step in range(1, possible_steps + 1):
        if _array_stepper(numbers, i + step, memo):
            memo[i] = True
            return True

    memo[i] = False
    return False


def array_stepper(numbers):
    memo = {}
    return _array_stepper(numbers, 0, memo)
