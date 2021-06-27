from itertools import combinations
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # Solution 1
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0 and s[0: len(s) - i] == s[i: ]:
                return True
        return False
        
        # Solution 2
        i = 1
        while i < len(s):
            j = i
            while j <= len(s):
                if len(s) % len(s[i-1: j]) == 0:
                    if len(s) != len(s[i-1: j]):
                        if s[i-1: j] * (len(s) // len(s[i-1: j])) == s:
                            return True
                j += 1
            i += 1
        return False
        
        # Solution 3 using inbuild combinations
        all_combos = [s[x:y] for x, y in combinations( 
            range(len(s) + 1), r = 2)] 
        for i in all_combos:
            if len(s) % len(i) == 0 and i != s:
                if i * (len(s) // len(i)) == s:
                    return True
        return False

        # Solution 4 using 2 while loops
        all_combos = []
        i = 0
        while i < len(s):
            j = i + 1
            while j <= len(s):
                all_combos.append(s[i : j])
                j += 1
            i += 1
        for i in all_combos:
            if len(s) % len(i) == 0 and i != s:
                if i * (len(s) // len(i)) == s:
                    return True
        return False
