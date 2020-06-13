Solution 1:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums.count(0) == len(nums):
            return nums
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums

Solution 2:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums.count(0) == len(nums):
            return nums
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        return nums
