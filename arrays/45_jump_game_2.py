from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        def jump(self, nums: List[int]) -> int:
            jumps = 0
            current_end = 0
            farthest = 0

            for i in range(len(nums) - 1):
                # Update the farthest point that can be reached
                farthest = max(farthest, i + nums[i])

                # If we have reached the end of the current jump range
                if i == current_end:
                    # We need to make another jump
                    jumps += 1
                    current_end = farthest

                # If the current end has reached or passed the last index, we can stop
                if current_end >= len(nums) - 1:
                    break

            return jumps

    # Testing
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    print(solution.jump(nums))  # Expected result: 2