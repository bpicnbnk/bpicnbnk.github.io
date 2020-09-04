from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix:
            n = len(matrix)
            m = len(matrix[0])
            row = n-1
            col = m-1
            while row > -1 and col > -1:
                if matrix[row][col] < target:
                    row += 1
                    col += 1
                elif matrix[row][col] > target:
                    row -= 1
                    col += 1
                else:
                    return True
        return False


s = Solution()
nums = [-1, 2, 1, -4]
t = 3
result = s.findNumberIn2DArray(nums, t)
print(result)
