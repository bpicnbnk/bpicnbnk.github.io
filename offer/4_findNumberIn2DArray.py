from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix:
            n = len(matrix)
            m = len(matrix[0])
            row = 0
            col = m-1
            # [1,   4,  7, 11, 15],
            # [2,   5,  8, 12, 19],
            # [3,   6,  9, 16, 22],
            # [10, 13, 14, 17, 24],
            # [18, 21, 23, 26, 30]
            while row < n and col > -1:
                if matrix[row][col] < target:
                    row += 1
                elif matrix[row][col] > target:
                    col -= 1
                else:
                    return True
        return False


s = Solution()
nums = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
result = s.findNumberIn2DArray(nums, target)
print(result)
