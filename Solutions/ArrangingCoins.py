class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n in (0, 1):
            return n
        elif n == 3:
            return 2
        else:
            rows = 0
            for sc in range(1, int(n/2) + 1):
                if n-sc < 0:
                    break
                rows += 1
                n -= sc
            return rows
