class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in set(nums):
            if nums.count(num) > len(nums)//2:
                return num
