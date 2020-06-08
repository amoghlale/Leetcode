from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerset_list = []
        for subset_length in range(len(nums)+1):
            for i in combinations(nums, subset_length):
                sorted_element_list = sorted(list(i))
                if sorted_element_list not in powerset_list:
                    powerset_list.append(sorted_element_list)
        return powerset_list
