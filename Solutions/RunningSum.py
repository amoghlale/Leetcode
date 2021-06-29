Solution 1 (using list comprehension and slicing):
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[: i]) for i in range(1, len(nums) + 1)]

Solution 2:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = nums[0]
        output_list = [nums[0]]
        for i in range(1, len(nums)):
            running_sum += nums[i]
            output_list.append(running_sum)
        return output_list
