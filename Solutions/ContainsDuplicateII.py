Solution 1 (using dict):
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ref_dict = {}
        for idx, num in enumerate(nums):
            if num in ref_dict and abs(idx - ref_dict[num]) <= k:
                return True
            ref_dict[num] = idx
        return False

Solution 2 (with slicing):
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums):
            if i + k + 1 > len(nums):
                upper_limit = len(nums)
            else:
                upper_limit = i + k + 1
            if nums[i: upper_limit].count(nums[i]) > 1:
                return True
            i += 1
        return False

        