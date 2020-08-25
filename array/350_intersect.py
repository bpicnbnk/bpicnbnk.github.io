from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = []
        for key in c1.keys():
            if key in c2.keys():
                num = c1[key] if c1[key] > c2[key] else c2[key]
                result.extend([c1[key]*num])
        return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        result = []
        for num in nums2:
            if num in c1.keys():
                if c1[num] > 0:
                    result.append(num)
                    c1[num] -= 1
        return result


s = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = s.intersect(nums1, nums2)
print(result)
