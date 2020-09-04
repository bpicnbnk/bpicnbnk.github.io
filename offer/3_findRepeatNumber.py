from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return i
        # return num


s = Solution()
nums = [-1, 2, 1, -4]
result = s.findRepeatNumber(nums)
print(result)
