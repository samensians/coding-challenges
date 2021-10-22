"""
Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    res = []
    nums.sort()
    # a + b + c = 0
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                # for each a there can be multiple solutions
                # increase left pointer to search for a new solution -c = a + nums[l]
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
