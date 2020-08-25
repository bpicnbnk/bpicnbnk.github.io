class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and len(set(s)) == len(set(t)):
            from collections import Counter
            sc = Counter(s)
            tc = Counter(t)
            for i in sc.keys():
                if i not in tc.keys() or sc[i] != tc[i]:
                    return False
            return True
        else:
            return False
