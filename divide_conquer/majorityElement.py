from typing import List


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        mainnum = 0
        countnum = 0
        left = 0
        right = left+1
        size = len(nums)
        while(left < size-1):
            if countnum == 0:
                if nums[left] == nums[right]:
                    mainnum = nums[left]
                    countnum += 2
            else:
                if nums[left] == nums[right]:
                    if mainnum == nums[left]:
                        countnum += 2
                    else:
                        countnum -= 2
            left += 2
            right = left+1

        if left == size-1:
            if not countnum:
                return nums[left]
        return mainnum


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 【不断切分的终止条件】
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        # 【准备数据，并将大问题拆分为小问题】
        left = self.majorityElement(nums[:len(nums)//2])
        right = self.majorityElement(nums[len(nums)//2:])
        # 【处理子问题，得到子结果】
        # 【对子结果进行合并 得到最终结果】
        if left == right:
            return left
        if nums.count(left) > nums.count(right):
            return left
        else:
            return right


s = Solution()
nums = [-1, 1, 1, 1, 2, 1]
nums = [1, 3, 1,2, 1, 4,1]
# nums=[32,32,58,32,32,32,32,32,50,77,77,32,32,32,51,32,61,32,32,88,44,32,7,32,32,92,28,1,32,32,44,97,99,32,1,40,32,20,32,68,85,32,32,32,32,98,13,32,32,7,74,32,32,52,32,86,28,45,73,19,32,32,27,32,83,32,68,94,32,32,32,32,27,24,32,32,96,32,99,60,46,32,22,71,25,32,32,32,32,53,54,26,32,32,32,32,13,32,23,6]

result = s.majorityElement(nums)
print(result)
