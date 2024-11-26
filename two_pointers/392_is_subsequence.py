class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_marker = 0
        t_pointer = 0
        if not s:
            return True
        while t_pointer < len(t):
            if t[t_pointer] == s[s_marker]:

                s_marker += 1
                if s_marker == len(s):
                    return True

            t_pointer += 1
        return False
s = "abc"
t = "ahbgdc"

solution = Solution()
k = solution.isSubsequence(s, t)
print(k)