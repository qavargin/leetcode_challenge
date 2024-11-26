from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            if numbers[start] + numbers[end] < target:
                start += 1
            if numbers[start] + numbers[end] > target:
                end -= 1

numbers = [2, 3, 4]
target = 6

solution = Solution()
k = solution.twoSum(numbers, target)
print(k)