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


s = Solution()
nums = 'babad'

result = s.longestPalindrome(nums)
print(result)
