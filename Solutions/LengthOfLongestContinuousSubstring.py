class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            substr = ""
            longest = ""
            for c in s:
                if c in substr:
                    substr = substr[substr.find(c) + 1: ]
                substr += c
                if len(longest) < len(substr):
                    longest = substr
            return len(longest)
