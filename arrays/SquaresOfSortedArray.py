"""
Given an integer array nums sorted in non-decreasing order, return an array of
the squares of each number sorted in non-decreasing order.
"""

def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(nlogn)
        """
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums
        """

        left, right = 0, len(nums) - 1
        decreasing_list = []
        while left <= right:
            left_val, right_val = abs(nums[left]), abs(nums[right])
            if left_val > right_val:
                decreasing_list.append(left_val**2)
                left += 1
            else:
                decreasing_list.append(right_val**2)
                right -= 1
        decreasing_list.reverse()
        return decreasing_list
