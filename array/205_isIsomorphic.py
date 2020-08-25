class Solution:
    def isIsomorphic(self, pattern: str, s: str) -> bool:
        if len(pattern) == len(s):
            p = []
            d = {}
            for i, j in zip(pattern, s):
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
ss = "foo"
t = "bar"
result = s.isIsomorphic(ss, t)
print(result)
