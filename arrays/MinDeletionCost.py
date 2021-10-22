"""
Given a string s and an array of integers cost where cost[i] is the cost of
deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical
letters next to each other.

Notice that you will delete the chosen characters at the same time, in other
words, after deleting a character, the costs of deleting other characters
will not change.
"""

def minCost(self, s: str, cost: List[int]) -> int:
    left, ans = 0, 0
    for right in range(1, len(s)):
        if s[left] == s[right]:
            if cost[left] < cost[right]:
                ans += cost[left]
            else:
                ans += cost[right]
                # If right is cheaper, delete right and kept left
                # position for next step calculation
                continue

        left = right
    return ans
