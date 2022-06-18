def five_sort(nums):
  i = 0
  j = len(nums) - 1

  while i < j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      # i += 1 - nice to have
    else:
      i += 1
  return nums

#   two ptrs
#     i - starts at idx 0, finds 5's
#     j - starts at last idx, find non-5's

#   iterate through nums
#     if j IS a 5
#       decrememnt j ptr
#     if i IS a 5
#       now i points to a non-5 and j points to a 5
#       swap items at ptrs i and j
#     else
#       incrememnt i ptr

# return nums
