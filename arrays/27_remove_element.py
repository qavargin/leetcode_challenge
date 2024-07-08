from typing import List
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are 
not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are 
not equal to val. The remaining elements of nums are not important as well as the size of nums.

Return k.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track the position for elements not equal to val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# Test this solution:
nums = [3, 2, 2, 3, 3]
val = 3
solution = Solution()
k = solution.removeElement(nums, val)
print(f"Modified nums: {nums[:k]}")  # Output: Modified nums: [2, 2]
print(f"Number of valid elements: {k}")  # Output: Number of valid elements: 2