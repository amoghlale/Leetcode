Solution 1:
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset_list = [list(i) for subset_length in range(len(nums)+1) for i in combinations(nums, subset_length)]
        return powerset_list

Solution 2:
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset_list = []
        for subset_length in range(len(nums)+1):
            for i in combinations(nums, subset_length):
                powerset_list.append(list(i))
        return powerset_list
