from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen:
            if nlen < 3:
                return max(nums)
        else:
            return 0
        maxnum = 0
        for index in range(nlen):
            now = nums[index]
            tmp = now
            for j in range(0, index-1):
                if now+nums[j] > tmp:
                    tmp = now+nums[j]
            nums[index] = tmp
            if tmp > maxnum:
                maxnum = tmp
        return maxnum

    def rob2(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen:
            if nlen < 3:
                return max(nums)
        else:
            return 0
        maxnum = 0
        dp = [0]*nlen
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for index in range(2, nlen):
            # dp[index] = max(dp[index-2]+nums[index], dp[index-1])
            dp[index] = dp[index-2]+nums[index] if dp[index-2] + \
                nums[index] > dp[index-1] else dp[index-1]
        return dp[-1]
        class Solution:

    def rob3(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen:
            if nlen < 3:
                return max(nums)
        else:
            return 0
        dp = [0]*3
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for index in nums[2:]:
            # dp[index] = max(dp[index-2]+nums[index], dp[index-1])
            dp[2] = dp[0]+index if dp[0] + \
                index > dp[1] else dp[1]
            dp[:2] = dp[1:]
        return dp[-1]


s = Solution()
nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
nums = [1, 2, 1, 2]

result = s.rob2(nums)
print(result)
