from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        volume = 0
        right_pointer = len(height) - 1
        while left_pointer < right_pointer:
            current = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
            if volume < current:
                volume = current
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return volume


height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
k = solution.maxArea(height)
print(k)