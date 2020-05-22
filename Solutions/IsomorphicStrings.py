class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            i = 0
            ref_dict = {}
            isomorphic_str = ""
            while i < len(s):
                if s[i] in ref_dict:
                    isomorphic_str += ref_dict[s[i]]
                elif t[i] in ref_dict.values():
                    isomorphic_str += s[i]
                else:
                    ref_dict[s[i]] = t[i]
                    isomorphic_str += ref_dict[s[i]]
                i += 1
            return True if isomorphic_str == t else False     
