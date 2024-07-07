from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # i and j - counters for both lists
        i = 0
        j = 0

        # run loop until we will move all elements
        while i < n:
            # check that nums1 element > nums2 element
            # check if we already on last element on nums1
            if j >= m + i or nums1[j] > nums2[i]:
                nums1.insert(j, nums2[i])
                nums1.pop()
                i += 1
            else:
                j += 1
# Test this solution:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]