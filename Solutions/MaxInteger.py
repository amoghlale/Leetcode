from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lambda_func = lambda x, y: 1 if str(x) + str(y) > str(y) + str(x) else -1
        sorted_str = ''.join(sorted(map(str, nums), key=cmp_to_key(lambda_func), reverse=True))
        return '0' if sorted_str[0] == '0' else sorted_str
