"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = ""
        i = 0
        j = 0
        start = -1
        while i < len(haystack):

            if haystack[i] == needle[j]:
                result += needle[j]
                j += 1
                if j == 1:
                    start = i
                i += 1
            else:
                j = 0
                i = start + 1
                start += 1
                result = ""
            if result == needle:
                return start
        return -1
needle = "issip"
haystack = "mississippi"
solution = Solution()
k = solution.strStr(haystack, needle)

print(k)