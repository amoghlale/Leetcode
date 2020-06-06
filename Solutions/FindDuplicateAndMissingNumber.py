class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        unique_set = set()
        output_list = []
        for elem in nums:
            if elem in unique_set:
                output_list.append(elem)
                break
            else:
                unique_set.add(elem)
        missing_num = output_list.append(list(set([i for i in range(1, len(nums)+1)]).difference(nums))[0])
        return output_list
