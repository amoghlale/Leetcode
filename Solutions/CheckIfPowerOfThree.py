class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        else:
            while(n != 1):
                if n % 3 != 0:
                    return False
                n = n // 3
            return True

Alternate Solution:
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            return True if str(math.log(n, 3)).split(".")[-1] == '0' else False
