"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
def maxSubArray(self, nums: List[int]) -> int:
    local_max = global_max = -10001
    for num in nums:
        local_max = max(num, local_max + num)
        global_max = max(local_max, global_max)
    return global_max
