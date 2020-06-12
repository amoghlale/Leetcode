# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = (0, n-1)
        while low <= high:
            mid = low + (high - low) // 2
            mid_value = mid + 1
            if guess(mid_value) == 0:
                return mid + 1
            elif guess(mid_value) == -1:
                high = mid - 1
            else:
                low = mid + 1
        return None
