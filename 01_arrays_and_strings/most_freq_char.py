def most_frequent_char(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    best = None

    for char in s:
        if best is None or count[best] < count[char]:
            best = char

    return best

#   intialize dictionary

#   iterate through s
#     for each char in s, create the key-value pair in dictionary if it DNE, initialized w/ value 0
#     incrememnt value for char in dictionary

#   initalize variable, best, to track char with highest frequence (value in dictionary) as we traverse through s
#   intialize value to None

#   iterate through s
#     if best is None or if best in dictionary is less than current char in dictionary
#       then we have a new best, reassign best to current char

#   return best
