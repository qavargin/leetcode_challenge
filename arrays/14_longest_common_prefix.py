from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        i = 0
        minimal_value = ""
        result = ""
        flag = True
        for item in strs:
            if len(item)<length:
                length = len(item)
                minimal_value = item
        print(length)

        if length == 0:
            return  result

        while i < length:
            for item in strs:
                if item[i] != minimal_value[i]:
                    flag = False

            if flag == False:
                break
            else:
                result += minimal_value[i]
            i += 1

        return result



s = ["", "kkjjjb"]
solution = Solution()
k = solution.longestCommonPrefix(s)
print("Minimal prefix", k)