class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        sum_set = set()
        square_sum_of_digits = 0
        while square_sum_of_digits != 1:
            square_sum_of_digits = sum(map(lambda x: int(x) ** 2, [i for i in str(n)]))
            if square_sum_of_digits == 1:
                return True
            if square_sum_of_digits in sum_set:
                return False
            else:
                sum_set.add(square_sum_of_digits)
            n = square_sum_of_digits
        return False 
