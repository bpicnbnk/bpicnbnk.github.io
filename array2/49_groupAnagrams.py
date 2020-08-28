from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        d = {}
        ready = set()
        for s in strs:
            if s not in ready:
                ischoose = False
                for key in d.keys():
                    if len(s) == len(key):
                        cc=Counter(s)
                        if len(cc)==d[key][1]:
                            issame=True
                            for letter,num in cc.items():
                                if d[key][0][letter]!=num:
                                    issame=False
                                    break
                            if issame:
                                d[key].append(s)
                                ischoose = True
                                break
                if not ischoose:
                    cc=Counter(s)
                    d[s] = [cc,len(cc),s]
                ready.add(s)
            else:
                for key,value in d.items():
                    if s in value:
                        d[key].append(s) 
        return [value[2:] for value in d.values()]


s = Solution()
nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
nums = ["abbbbbbbbbbb", "aaaaaaaaaaab"]
# nums = ["",""]
result = s.groupAnagrams(nums)
print(result)
