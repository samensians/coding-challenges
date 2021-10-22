"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []
    product = 1
    n = len(nums)
    for i in range(0, n):
        answer.append(product)
        product *= nums[i]

    product = 1
    for i in range(n - 1, -1, -1):
        answer[i] = answer[i] * product
        product *= nums[i]
    return answer
