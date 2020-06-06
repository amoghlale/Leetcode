Solution 1:
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            unique_set = set()
            for elem in nums:
                if elem in unique_set:
                    return elem
                else:
                    unique_set.add(elem)

Solution 2:
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            for i in set(nums):
                if nums.count(i) > 1:
                    return i

