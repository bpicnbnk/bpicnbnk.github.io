# 题目
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。

 

提示：

1 <= s.length <= 1000
s 只包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码
从字符串尾部开始向前比较
```
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        slen = len(s)
        if slen < 2:
            return slen
        dp = [[0]*slen for _ in range(slen)]
        # maxlen = 0
        for i in range(slen):
            dp[i][i] = 1
        for i in range(slen, -1, -1):
            for j in range(i+1, slen):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                # if dp[i][j] > maxlen:
                #     maxlen = dp[i][j]
        return dp[0][-1]
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
