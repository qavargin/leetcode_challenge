from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                flag = 0
            elif flag == 0:
                nums[k] = nums[i]
                k += 1
                flag = 1
        return k

# Test this solution:
nums = [1, 1, 1, 2, 2, 3]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Modified nums: {nums[:k]}")
