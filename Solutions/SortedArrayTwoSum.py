Solution 1: using 2 pointers i and j (faster than 99.30% of solutions)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i <= j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

Solution 2: using dictionary
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index_dict = {}
        for index_val, num_val in enumerate(numbers):
            if num_val in num_index_dict:
                return [num_index_dict[num_val], index_val + 1]
            else:
                num_index_dict[target-num_val] = index_val + 1
