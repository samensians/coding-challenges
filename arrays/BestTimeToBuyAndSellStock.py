"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""

def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price_seen = 10000
    for i in range(len(prices)):
        min_price_seen = min(prices[i], min_price_seen)
        profit = prices[i] - min_price_seen
        max_profit = max(profit, max_profit)
    return max_profit
