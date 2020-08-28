from typing import List


class Solution:
    def fourSum(self, nums: List[int], mytarget: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # c 对应的指针初始指向数组的最右端
                fourth = n - 1
                target = mytarget-nums[first]-nums[second]
                # 枚举 b
                for third in range(second + 1, n):
                    # 需要和上一次枚举的数不相同
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue
                    # 需要保证 b 的指针在 c 的指针的左侧
                    while third < fourth and nums[third] + nums[fourth] > target:
                        fourth -= 1
                    # 如果指针重合，随着 b 后续的增加
                    # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                    if third == fourth:
                        break
                    if nums[third] + nums[fourth] == target:
                        ans.append([nums[first], nums[second],
                                    nums[third], nums[fourth]])

        return ans


s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = s.fourSum(nums, target)
print(result)
