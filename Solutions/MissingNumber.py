class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([i for i in range(len(nums)+1)]) - sum(nums) if len(nums) > 0 else 0
