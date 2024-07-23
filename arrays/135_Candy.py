from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1

        n = len(ratings)
        left = [1] * n
        right = [1] * n

        # set rewards from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # set rewards from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # calculate maximum
        total_candies = 0
        for i in range(n):
            total_candies += max(left[i], right[i])

        return total_candies
ratings = [7,6,5,4,3,2,1]
solution = Solution()
k = solution.candy(ratings)
print("New array:", k)