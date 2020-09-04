from typing import List


class Solution:
    def getmatrix(self, num):
        m = [[0]*num for _ in range(num)]
        i = 1
        row = 0
        col = 0
        while i < num**2+1:
            while row < num and col < num and m[row][col] == 0:
                m[row][col] = i
                i += 1
                col += 1
            col -= 1
            row += 1
            while row < num and col < num and m[row][col] == 0:
                m[row][col] = i
                i += 1
                row += 1
            row -= 1
            col -= 1
            while row < num and col > -1 and m[row][col] == 0:
                m[row][col] = i
                i += 1
                col -= 1
            col += 1
            row -= 1
            while row > 0 and col < num and m[row][col] == 0:
                m[row][col] = i
                i += 1
                row -= 1
            row += 1
            col += 1
        return m

s = Solution()
nums = 7
result = s.getmatrix(nums)
print(result)
for i in result:
    print(i)
