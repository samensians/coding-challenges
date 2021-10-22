"""
Given an integer array nums, find a contiguous non-empty subarray within the
array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""

def maxProduct(self, nums: List[int]) -> int:
    global_max = float("-inf")
    local_max = local_min = 1
    for num in nums:
        temp = local_max
        local_max = max(num, local_min * num, temp * num)
        local_min = min(num, local_min * num, temp * num)
        global_max = max(local_max, global_max)
    return global_max
