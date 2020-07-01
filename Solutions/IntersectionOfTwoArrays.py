Solution 1:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output_set = set()
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    output_set.add(i)
        else:
            for i in nums1:
                if i in nums2:
                    output_set.add(i)
        return output_set

Solution 2:
class Solution:
    def find_intersection(self, bigger, smaller):
        output_set = set()
        for i in smaller:
            if i in bigger:
                output_set.add(i)
        return output_set

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
            return self.find_intersection(nums1, nums2) if len(nums1) > len(nums2) else self.find_intersection(nums2, nums1)
