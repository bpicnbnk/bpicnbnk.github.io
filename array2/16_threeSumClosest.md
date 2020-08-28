# 题目
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
```
class Solution:
    def threeSumClosest(self, nums: List[int], mytarget: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        nmin = float('inf')

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = mytarget-nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    if second!=n-1:
                        third = second+1
                        tmp = nums[second] + nums[third] - target
                        if nmin > abs(tmp):
                            nmin = abs(tmp)
                            ans = tmp+mytarget
                    break
                # 小于等于
                if nums[second] + nums[third] == target:
                    return mytarget
                else:
                    less=nums[second] + nums[third] - target
                    if third!=n-1:
                        more=nums[second] + nums[third+1] - target
                        less =less if abs(less)<abs(more) else more
                    if nmin > abs(less):
                        nmin = abs(less)
                        ans = less+mytarget
        return ans
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
