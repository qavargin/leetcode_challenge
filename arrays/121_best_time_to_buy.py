from typing import List
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # if current price < min price we will update best buy price
            if price < min_price:
                min_price = price

            # if max profit increased we will update it
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

# Testing:
nums = [7,1,5,3,6,4]
solution = Solution()
k = solution.maxProfit(nums)
print("Maxprofit:", k)