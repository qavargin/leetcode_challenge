from typing import List
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same. 

Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following 
things:

Change the array nums such that the first k elements of nums contain the unique elements in the order
they were present in nums initially. The remaining elements of nums are not important as well as the 
size of nums.
Return k.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        element = ""
        while i < len(nums):
            if nums[i] == element:
                nums.pop(i)
            else:
                element = nums[i]
                i+=1
        k = len(nums)
        return k
# Test this solution:
nums = [1, 1, 2]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Modified nums: {nums}")  # Output: Modified nums: [2, 2]
