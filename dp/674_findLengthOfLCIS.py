from typing import List


class Solution1:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen == 1:
            return 1
        slist = [1]*nlen
        for index in range(1, nlen):
            now = nums[index]
            pre = nums[index-1]
            if now > pre:
                slist[index] = slist[index-1]+1
            elif now == pre:
                slist[index] = slist[index-1]
            else:
                for i in range(index):
                    pre = nums[i]
                    if now > pre:
                        slist[index] = max(slist[index], slist[i]+1)
                    elif now == pre:
                        slist[index] = max(slist[index], slist[i])
        return max(slist)


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen < 2:
            return nlen
        pre = nums[0]
        tmp = 1
        maxlen = 0
        for num in nums[1:]:
            if num > pre:
                tmp += 1
            else:
                if maxlen < tmp:
                    maxlen = tmp
                # maxlen = max(maxlen, tmp)
                tmp = 1
            pre = num
        maxlen = max(maxlen, tmp)
        return maxlen

    def findLengthOfLCIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0  # 判断边界条件
        dp = [1]*len(nums)  # 初始化dp数组状态
        # 注意需要得到前一个数，所以从1开始遍历，否则会超出范围
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:  # 根据题目所求得到状态转移方程
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 1
        return max(dp)  # 确定输出状态


s = Solution()
nums = [1, 3, 5, 4, 7]

result = s.findLengthOfLCIS(nums)
print(result)
result = s.findLengthOfLCIS2(nums)
print(result)
