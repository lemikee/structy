def intersection(a, b):
    set_b = set(b)
    result = []

    for item in a:
        if item in set_b:
            result.append(item)

    return result

    #  we can do this in O(n^2) but using a set we can do better

    # create set of list b, sets have O(1) look up time

    # iterate through a
    #   check if current item is in set_b
    #   if it is, add it to result list

    # return result list
