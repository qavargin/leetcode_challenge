from typing import List
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i in range(len(nums) - 1):
            if nums[i] >= jump:
                jump = nums[i
            else:
                jump-=1
            if jump == 0:
                return False

        return True
nums = [2,3,1,1,4]
solution = Solution()
k = solution.canJump(nums)
