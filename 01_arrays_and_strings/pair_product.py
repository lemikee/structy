def pair_product(numbers, target_product):
    prev_nums = {}

    for index, current_num in enumerate(numbers):
        complement = target_product // current_num

        if complement in prev_nums:
            return (index, prev_nums[complement])
        prev_nums[current_num] = index
