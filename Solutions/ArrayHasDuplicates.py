Solution 1:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False

Solution 2:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result_set = set()
        for i in nums:
            if i in result_set:
                return True
            result_set.add(i)
        return False
