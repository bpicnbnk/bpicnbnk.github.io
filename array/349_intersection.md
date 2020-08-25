# 题目
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
 

说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
```
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = []
        for i in nums2:
            if i not in result:
                if i in set1:
                    result.append(i)
        return result

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return set2 & set1

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        return set([i for i in nums2 if i in nums1])
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
set判断存在效率比if高。无value的hash实现，O(1)时间复杂度。