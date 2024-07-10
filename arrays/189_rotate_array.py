from typing import List
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        length = len(nums)
        result = nums[:]
        for i in range(len(nums)):

            # we need to set value in element with new position
            nums[(i + k) % length] = result[i]


# Test:
nums = [1, 2, 3, 4, 5, 6, 7]
k=3
solution = Solution()
output = solution.rotate(nums, k)
print(nums)
