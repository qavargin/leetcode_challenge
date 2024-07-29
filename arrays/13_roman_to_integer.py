"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        event_date = list(s)
        i = 0
        count = 0
        while len(event_date) > 0:
            if len(event_date) > 0 and event_date[0] == 'M':
                count += 1000
                del event_date[0]
            if len(event_date) > 0 and event_date[0] == 'D':
                count += 500
                del event_date[0]
            if len(event_date) > 0 and event_date[0] == 'L':
                count += 50
                del event_date[0]
            if len(event_date) > 0 and event_date[0] == 'V':
                count += 5
                del event_date[0]


            if len(event_date)>0 and event_date[0] == 'C':
                if len(event_date)>1 and event_date[1] == 'M':
                    count += 900
                    del event_date[:2]

                elif len(event_date)>1 and event_date[1] == 'D':
                    count += 400
                    del event_date[:2]
                else:
                    count += 100
                    del event_date[0]

            if len(event_date)>0 and event_date[0] == 'X':
                if len(event_date) > 1 and event_date[1] == 'L':
                    count += 40
                    del event_date[:2]

                elif len(event_date) > 1 and event_date[1] == 'C':
                    count += 90
                    del event_date[:2]
                else:
                    count += 10
                    del event_date[0]

            if len(event_date)>0 and event_date[0] == 'I':
                if len(event_date) > 1 and event_date[1] == 'V':
                    count += 4
                    del event_date[:2]

                elif len(event_date) > 1 and event_date[1] == 'X':
                    count += 9
                    del event_date[:2]
                else:
                    count += 1
                    del event_date[0]


        return count


s = "MDL"
solution = Solution()
k = solution.romanToInt(s)
print("Year:", k)

