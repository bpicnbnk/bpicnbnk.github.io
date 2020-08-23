# 题目
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路及实现代码

```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1 > word2
        word1len = len(word1)
        word2len = len(word2)
        dp = [[0]*(word2len+1) for i in range(word1len+1)]
        for i in range(word2len+1):
            dp[0][i] = i

        for i in range(word1len+1):
            dp[i][0] = i
        for i in range(1, word1len+1):
            for j in range(1, word2len+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 分别对应删除，添加和替换操作
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1]
                                   [j-1])+1
        return dp[-1][-1]
```
- 其他解法参考<a href="">地址</a>
``` 

``` 
# 总结归纳
