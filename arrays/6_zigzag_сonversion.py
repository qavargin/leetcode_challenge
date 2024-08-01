class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        rows = 0
        direction = "Down"
        for char in s:
            zigzag[rows].append(char)
            if direction == "Down":
                if rows < numRows - 1:
                    rows += 1
                else:
                    direction = "Up"
                    rows -= 1

            elif direction == "Up":
                if rows > 0:
                    rows -= 1
                else:
                    direction = "Down"
                    rows += 1


        result = "".join(["".join(row) for row in zigzag])
        return result

origial = "PAYPALISHIRING"
solution = Solution()
k = solution.convert(origial, 3)
print("Zigzag:", k)