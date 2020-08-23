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


s = Solution()
nums = 'bbbab'
nums = 'cbbd'

result = s.longestPalindromeSubseq(nums)
print(result)
