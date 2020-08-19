# 题目
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。所以不相等的两个数就可以跳过，最后必然剩余多数元素。
```
class Solution:
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
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
“多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。”这个条件很重要。