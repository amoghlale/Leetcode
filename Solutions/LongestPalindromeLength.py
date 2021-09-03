from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        a => longest length of palindrome 1
        ab => longest length 1, aa=> longest length 2
        aab=> longest length 3 (aba)
        aabb => longest length 4 (abba or baab)
        """
        char_count_dict = Counter(s)
        longest = 0
        for char, count in char_count_dict.items():
            longest += (count // 2) * 2
        return min(len(s), longest + 1)
