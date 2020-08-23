# 题目
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
中心向两边扩散
```
class Solution:
    def __init__(self):
        self.s = ''
        self.slen = 0

    def lengpalindrome(self, i, j):
        num = 0
        while i > -1 and j < self.slen and self.s[i] == self.s[j]:
            if i == j:
                num += 1
            else:
                num += 2
            i -= 1
            j += 1
        return num

    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        if slen < 2:
            return s
        self.s = s
        self.slen = slen
        maxlen = 0
        begin = 0
        for i in range(slen-1):
            olen = self.lengpalindrome(i, i)
            tlen = self.lengpalindrome(i, i+1)
            # if olen > tlen:
            #     begin = i-(olen-1)//2
            # else:
            #     begin = i-(tlen-1)//2
            tmp = max(olen, tlen)
            if tmp > maxlen:
                begin = i-(tmp-1)//2
                maxlen = max(maxlen, tmp)
        return s[begin:begin+maxlen]
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
