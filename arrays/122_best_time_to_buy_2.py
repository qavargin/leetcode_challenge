from typing import List
"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        price = float('inf')
        for item in prices:
            if item < price:
                price = item
            else:
                profit += item - price
                price = item

        return profit

# Testing:
nums = [7,1,5,3,6,4]
solution = Solution()
k = solution.maxProfit(nums)
print("Maxprofit:", k)