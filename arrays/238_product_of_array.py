from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        index = 1
        prefix = 1
        result = [1] * length
        left = [1] * length
        right = [1] * length
        for i in range(1, length):
            prefix *= nums[i-1]
            left[i] = prefix
        for i in range(length-2, -1, -1):
            index *= nums[i + 1]
            right[i] = index
        for i in range(length):
            result[i] = left[i] * right[i]
        return result

nums = [1, 2, 3, 4]
solution = Solution()
k = solution.productExceptSelf(nums)
print("New array:", k)