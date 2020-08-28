# 题目
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
```
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
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
