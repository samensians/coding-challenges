"""
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        elif mid_value > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
