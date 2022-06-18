def pair_sum(numbers, target_sum):
    prev_nums = {}

    for i, num in enumerate(numbers):
        complement = target_sum - num
        if complement in prev_nums:
            return (i, prev_nums[complement])
        prev_nums[num] = i

    return null

#   intialize dictionary, prev_nums, to track previously seen numbers, key is num, value is index

#   iterate through numbers with index, enumerate
#     get complement needed for current num to sum to target_sum

#     check if complement in prev_nums dictionary
#       if it is, then return current index and index of complement/value in prev_nums in tuple
#     if not, create the key-value pair for current num in prev_nums

#   return null
