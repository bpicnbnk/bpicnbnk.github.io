from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, i in enumerate(nums):
            if target-i in d.keys():
                return [d[target-i], index]
            if i not in d.keys():
                d[i] = index
