class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            max_current = nums[0]
            max_global = nums[0]
            for i in range(1, len(nums)):
                max_current = max(nums[i], max_current+nums[i])
                if max_current > max_global:
                    max_global = max_current
            return max_global
