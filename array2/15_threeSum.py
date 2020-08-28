from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        d={}
        new=[]
        for i in nums:
            if i not in d:
                d[i]=0
                new.append(i)
            elif d[i]<2:
                d[i]+=1
                new.append(i)
        r = []
        # cha=set()
        s = set()
        for i, j,k in combinations(new, 3):
            if ((i, j) not in s) and ((j, i) not in s) and i+j+k == 0:
                r.append([i, j, k])
                for m, n in combinations([i, j, k], 2):
                    s.add((m, n))
        return r


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
nums = [9,-9,4,12,12,0,-14,-7,10,-1,11,-10,-3,2,-9,0,8,-9,-5,-1,10,5,13,-5,-9,-12,9,-3,10,10,-10,4,8,1,-7,-2,-14,-6,6,11,8,-6,9,13,11,7,-10,-4,14,0,3,1,-10,-7,3,-12,-3,-11,0,-8,-15,5,3,8,13,11,13,-15,-9,4,3,6,5,-11,-4,-6,4,1,5,-5,-13,-7,11,-8,2,-1,-12,14,3,3,13,-5,-14,-7,11,14,-11,9,6,-13,-9,-13,1,11,-9,12,-10,2,-1,3,12,-7,3,0,0,12,6,3,3,-13,14,1,-3]
result = s.threeSum(nums)
print(result)
