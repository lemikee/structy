def permutations(items):
    if len(items) == 0:
        return [[]]

    first = items[0]

    perms_without_first = permutations(items[1:])
    perms_with_first = []

    for perm in perms_without_first:
        for index in range(0, len(perm) + 1):
            perms_with_first.append([*perm[0:index], first, *perm[index:]])

    return perms_with_first
