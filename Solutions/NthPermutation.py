from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(map(str, sorted(list(permutations([i for i in range(1, n+1)], n)))[k-1]))
