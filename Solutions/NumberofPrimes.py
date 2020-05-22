import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 <= n < 3:
            return 0
        else:
            prime_flag = [0, 0] + (n-2) * [1]
            for i in range(2, int(round(math.sqrt(n)))+1):
                for j in range(i * 2, n, i):
                    prime_flag[j] = 0
            return prime_flag.count(1)
