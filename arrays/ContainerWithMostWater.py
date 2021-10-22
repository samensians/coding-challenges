"""
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

def maxArea(self, height: List[int]) -> int:
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        if area > res:
            res = area

        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return res
