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
