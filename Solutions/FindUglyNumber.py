class Solution:
    def findFactors(self, num, ugly_no, factors):
        if num > ugly_no and num % ugly_no == 0:
            while num % ugly_no == 0:
                    num = num // ugly_no
                    factors.append(ugly_no)
        return num

    def isUgly(self, num: int) -> bool:
        factors = []
        ugly_nos = [2, 3, 5]
        for ugly_no in ugly_nos:
            num = self.findFactors(num, ugly_no, factors)
        return True if num == 1 or num in ugly_nos else False 
