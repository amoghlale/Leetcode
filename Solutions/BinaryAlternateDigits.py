class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        i, j = 0, 1
        binary_repr = bin(n)[2: ]
        while i <= len(binary_repr) - 1 and j <= len(binary_repr):
            if j == len(binary_repr):
                break
            if binary_repr[i] == binary_repr[j]:
                return False
            i += 1
            j += 1
        return True
