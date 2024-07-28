from typing import List
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        # Заполняем массивы left_max и right_max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Вычисляем общий объем воды
        water_trapped = 0
        for i in range(n):
            water_trapped += min(left_max[i], right_max[i]) - height[i]

        return water_trapped



height = [2,0,1]
solution = Solution()
k = solution.trap(height)
print("Water volume:", k)