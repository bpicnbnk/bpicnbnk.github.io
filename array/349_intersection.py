class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = []
        for i in nums2:
            if i not in result:
                if i in set1:
                    result.append(i)
        return result

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return set2 & set1

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        return set([i for i in nums2 if i in nums1])
