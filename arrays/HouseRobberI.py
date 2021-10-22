"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.
"""

from typing import List

def rob(nums: List[int], i: int) -> int:
    if i >= len(nums):
        return 0
    else:
        return max(nums[i] + rob(nums, i + 2), rob(nums, i + 1))


def house_robber(nums: List[int]) -> int:
    i = 0
    return rob(nums, i)


if __name__ == "__main__":
    print(house_robber([2, 7, 9, 3, 1]))  # answer = 12
