class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s)-1

        while start < last:
            if s[start] == s[last]:
                start += 1
                last -= 1
            else:
                return False

        return True
