class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output_list = []
        unique_elements = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in unique_elements:
                output_list.append(i)
        return output_list
