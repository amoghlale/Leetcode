Solution 1 (optimized using left shift and right shift):
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative_output = False
        if dividend * divisor < 0:
            negative_output = True
	mask = 1
        quotient = 0
        dividend, divisor = (abs(dividend), abs(divisor))
        while divisor <= dividend:
            divisor <<= 1
            mask <<= 1
        while mask > 1:
            divisor >>= 1
            mask >>= 1
            if dividend >= divisor:
                dividend -= divisor
                quotient |= mask
        if negative_output and quotient > 2**31 - 1:
            return -2**31
        elif negative_output and quotient <= 2**31 - 1:
            return -quotient
        elif not negative_output and quotient > 2**31 - 1:
            return 2**31 - 1
        else:
            return quotient

Solution 2 (using + and -):
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative_output = False
        if dividend * divisor < 0:
            negative_output = True
        dividend, divisor = (abs(dividend), abs(divisor))
        quotient = 0
        while dividend - divisor >= 0:
            dividend -= divisor
            quotient +=1
        if negative_number == 1:
            return -abs(quotient)
        return abs(quotient)
