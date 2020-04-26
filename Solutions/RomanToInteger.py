class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        prefix_rules = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        total_sum = 0
        i = 0
        j = 0
        while i < len(s):
            j = i + 1
            if j < len(s) and s[i] in prefix_rules and s[j] in prefix_rules[s[i]]:
                total_sum += symbols[s[i]+s[j]]
                i += 2
            else:
                total_sum += symbols[s[i]]
                i += 1
        return total_sum
