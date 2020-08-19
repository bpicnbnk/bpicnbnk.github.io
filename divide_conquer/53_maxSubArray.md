# 题目
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
维护两个值：maxnum：连续子数组的最大和；pre：到nums[n]时，包括nums[n-1]的连续子数组的最大和pre。

到nums[n]时，更新两个值。

```
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
```
- 解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
这个题是求连续子数组的最大和，用分治左右分开处理，再处理两部分连接处，感觉是比较麻烦的。