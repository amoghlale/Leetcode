class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum_of_num = 0
        for val in range(1, round(num ** 0.5) + 1):
            if num % val == 0:
                sum_of_num += val
                if val != 1:
                    sum_of_num += (num // val)
        return sum_of_num == num
