def compress(s):
    s += '!'
    i = 0
    j = 0
    result = []

    while j < len(s):
        if s[i] != s[j]:
            num = j - i
            char = s[i]
            if num == 1:
                result.append(char)
            else:
                result.append(str(num) + char)
            i = j
        j += 1

    return ''.join(result)


#   two ptrs
#     i tracks start of group
#     j tries to find end of group

#   iterate through s
#     if char at i is not equal to char at j
#       then we know that we have a new group
#       get num times char at i is repeated
#       add num and char at i to result array
#       DONT add num if num is 1
#       i = j
#     else
#       j has not found end of group (by finding start of new group)
#       and we need to incrememnt j
#   return result joined by empty string
