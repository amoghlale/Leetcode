import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num > 0:
            return True if str(math.log(num, 4)).split(".")[-1] == "0" else False
