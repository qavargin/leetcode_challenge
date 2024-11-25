from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        new_row = []
        row_length = 0

        for word in words:
            if row_length + len(new_row) + len(word) > maxWidth:
                # Формируем строку с пробелами
                for i in range(maxWidth - row_length):
                    new_row[i % (len(new_row) - 1 or 1)] += ' '
                result.append(''.join(new_row))
                new_row = []
                row_length = 0

            new_row.append(word)
            row_length += len(word)

        # Обрабатываем последнюю строку
        result.append(' '.join(new_row).ljust(maxWidth))

        return result


origial = ["This", "is", "an", "example", "of", "text", "justification."]
solution = Solution()
k = solution.fullJustify(origial, 16)
print(k)
