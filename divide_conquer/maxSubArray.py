from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxnum = nums[0]
        pre = float('-inf')
        for nim in nums:
            pre = pre+nim if pre+nim > nim else nim
            maxnum = max(maxnum, pre)
        return maxnum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, 1]
result = s.maxSubArray(nums)
print(result)
