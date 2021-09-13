class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low = 0
        high = num
        while low <= high:
            mid = low + ((high-low) // 2)
            if mid**2 == num:
                return True
            if mid**2 < num:
                low = mid + 1
            if mid**2 > num:
                high = mid - 1
        return False
