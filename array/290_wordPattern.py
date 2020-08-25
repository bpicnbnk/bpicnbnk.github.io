class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        if len(pattern) == len(slist):
            p = []
            d = {}
            for i, j in zip(pattern, slist):
                if i not in d.keys():
                    if j not in d.values():
                        d[i] = j
                    else:
                        return False
                elif d[i] != j:
                    return False
            return True
        else:
            return False


s = Solution()
pattern = "abba"
st = "dog cat cat dog"
pattern = "abba"
st = "dog dog dog dog"
result = s.wordPattern(pattern, st)
print(result)
