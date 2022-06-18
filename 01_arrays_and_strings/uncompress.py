def uncompress(s):
    result = []

    i = 0
    j = 0

    while j < len(s):
        if s[j].isalpha():
            num = s[i:j]
            char = s[j]
            uncompressed_group = int(num) * char
            result.append(uncompressed_group)
            j += 1
            i = j
        else:
            j += 1
    return ''.join(result)


#   two pointers
#     i - finds start of group
#     j - finds end of group

# initialize both i and j ptrs, set to 0
# iterate through string
#   check if j ptr is alphabetical
#     if it is, then form uncompressed string which is num at string[j - i] * char at string[j]
#     push the uncompressed version to a list
#     increment j, j will be at start of a new group
#     catch j up to i
#
#    else, increment j ptr until string[j] is alphabetical
#  return results array joined
