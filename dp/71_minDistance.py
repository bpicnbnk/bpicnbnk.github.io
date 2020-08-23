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


s = Solution()
word1 = "horse"
word2 = "ros"

result = s.minDistance(word1, word2)
print(result)
