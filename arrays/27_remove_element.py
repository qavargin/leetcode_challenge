from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track the position for elements not equal to val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# Test this solution:
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
k = solution.removeElement(nums, val)
print(f"Modified nums: {nums[:k]}")  # Output: Modified nums: [2, 2]
print(f"Number of valid elements: {k}")  # Output: Number of valid elements: 2