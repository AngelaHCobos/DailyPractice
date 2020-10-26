def longest_consecutive(nums):
    nums.sort()
    previous = 0
    counter = 0
    max_counter = 0
    for x in nums:
        if previous + 1 == x:
            counter += 1
        else:
            if counter > max_counter:
                max_counter = counter
            counter = 0
        previous = x
    if counter > max_counter:
        max_counter = counter
    return max_counter


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4