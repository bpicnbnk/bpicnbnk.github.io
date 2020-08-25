class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        s = ''
        for (key, num) in c.most_common():
            s += key*num
        return s


s = Solution()
ss = "foo"
result = s.frequencySort(ss)
print(result)
