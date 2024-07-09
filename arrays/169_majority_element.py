from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

# Test this solution:
nums = [1, 1, 1, 2, 2, 3, 4, 1, 1]
solution = Solution()
k = solution.majorityElement(nums)
print(f"Modified nums: {nums[:k]}")