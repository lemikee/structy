def anagrams(s1, s2):
    return count(s1) == count(s2)


def count(s):
    counter = {}

    for char in s:
        if char not in counter:
            counter[char] = 0
        counter[char] += 1

    return counter
