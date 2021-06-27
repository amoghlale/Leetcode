Solution 1 O(n^2):
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        else:
            output_list = []
            nums = sorted(nums)
            for i in range(len(nums)-2):
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in output_list:
                            output_list.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
            return output_list

Solution 2 O(n^3):
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        if len(nums) < 3:
            return []
        else:
            intermediate_list = []
            for i in range(len(nums) - 2):
                for j in range(i+1, len(nums) - 1):
                    for k in range(j+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == 0:
                            intermediate_list.append(
                                sorted([nums[i], nums[j], nums[k]]))
            output_list = []
            for i, j, k in intermediate_list:
                if [i, j, k] not in output_list:
                    output_list.append([i, j, k])
            return output_list
