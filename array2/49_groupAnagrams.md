# 题目
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        d = {}
        ready = set()
        for s in strs:
            if s not in ready:
                ischoose = False
                for key in d.keys():
                    if len(s) == len(key):
                        cc=Counter(s)
                        if len(cc)==d[key][1]:
                            issame=True
                            for letter,num in cc.items():
                                if d[key][0][letter]!=num:
                                    issame=False
                                    break
                            if issame:
                                d[key].append(s)
                                ischoose = True
                                break
                if not ischoose:
                    cc=Counter(s)
                    d[s] = [cc,len(cc),s]
                ready.add(s)
            else:
                for key,value in d.items():
                    if s in value:
                        d[key].append(s) 
        return [value[2:] for value in d.values()]
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
超时了。。。