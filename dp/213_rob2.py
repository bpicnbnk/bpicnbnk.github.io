from typing import List


class Solution:
    def rob2(self, nums: List[int]) -> int:
        nlen = len(nums)
        dp = [0]*nlen
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for index in range(2, nlen):
            # dp[index] = max(dp[index-2]+nums[index], dp[index-1])
            dp[index] = dp[index-2]+nums[index] if dp[index-2] + \
                nums[index] > dp[index-1] else dp[index-1]
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen:
            if nlen < 3:
                return max(nums)
        else:
            return 0
        # if nums[0] == nums[-1]:
        #     return self.rob2(nums[:-1])
        b=self.rob2(nums[1:])
        f=self.rob2(nums[:-1])
        return b if b>f else f
        return self.rob2(nums[:-1]) if self.rob2(nums[:-1]) > self.rob2(nums[1:]) else self.rob2(nums[1:])


s = Solution()
nums = [1, 2, 1, 1]

result = s.rob(nums)
print(result)
