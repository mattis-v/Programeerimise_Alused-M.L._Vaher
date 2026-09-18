def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]

print(1, same_first_last([1,2,3]))