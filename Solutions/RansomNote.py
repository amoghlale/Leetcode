Solution 1:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) == 0 and len(ransomNote) == 0:
            return True
        else:
            letter_count_mapping = dict(zip([char for char in set(magazine)], [magazine.count(char) for char in set(magazine)]))
            for char in ransomNote:
                if char not in letter_count_mapping or letter_count_mapping[char] == 0:
                    return False
                else:
                    letter_count_mapping[char] -= 1
            return True

Solution 2:
from itertools import permutations
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        all_combinations = [list(permutations(magazine, i)) for i in range(len(magazine) + 1)]
        flatten_list = [item for sublist in all_combinations for item in sublist]
        join_flatten_list = [''.join(tups) for tups in flatten_list]
        for combo in join_flatten_list:
            if combo == ransomNote:
                return True
        return False
