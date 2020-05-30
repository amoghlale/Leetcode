from string import ascii_lowercase
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            alphabet_dict = dict(zip(ascii_lowercase, [0] * 26))
            for i in s:
                alphabet_dict[i] += 1
            for j in t:
                if alphabet_dict[j] == 0:
                    return False
                alphabet_dict[j] -= 1
            return True
