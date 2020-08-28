# 题目
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        d={}
        new=[]
        for i in nums:
            if i not in d:
                d[i]=0
                new.append(i)
            elif d[i]<2:
                d[i]+=1
                new.append(i)
        r = []
        # cha=set()
        s = set()
        for i, j,k in combinations(new, 3):
            if ((i, j) not in s) and ((j, i) not in s) and i+j+k == 0:
                r.append([i, j, k])
                for m, n in combinations([i, j, k], 2):
                    s.add((m, n))
        return r
```
- 其他解法参考<a href="https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/">地址</a>
``` 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
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
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans
``` 
# 总结归纳
时间超了，O(n**3)复杂度太高。

采用for + while的形式来处理三索引

处理重复值的套路：先转换为有序数组，再循环判断其与上一次值是否重复

对撞指针：先排序再对撞