class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            output_list = []
            for i in range(3):
                val = max(nums)
                output_list.append(val)
                nums.remove(val)
            return output_list[2]
