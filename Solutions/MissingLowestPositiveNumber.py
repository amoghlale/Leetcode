class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1 or (len(nums) == 1 and nums[0] != 1):
            return 1
        elif len(nums) == 1 and nums[0] == 1:
            return 2
        else:
            for i in range(1, len(nums)+2):
                if i not in nums:
                    return i
