"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    solution_dict = {}
    for idx, val in enumerate(nums):
        remainder = target - val
        if remainder in solution_dict:
            return [solution_dict[remainder], idx]
        else:
            solution_dict[val] = idx
