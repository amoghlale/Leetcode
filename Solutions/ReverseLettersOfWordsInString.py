Solution 1: Using 2 pointers starting from end
class Solution:
    def reverseWords(self, s: str) -> str:
        output_str = ""
        i = len(s) - 1
        j = len(s) - 2
        while j >= 0 and i >= 1:
            if s[j] == ' ':
                output_str = ' ' + s[i:j:-1] + output_str
                i = j - 1
                j -= 1
            j -= 1
        return s[i::-1] + output_str

Solution 2: using 2 pointers starting from 0
class Solution:
    def reverseWords(self, s: str) -> str:
        output_string = ''
        i = 0
        j = 1
        while i <= len(s) - 2 and j < len(s):
            if s[j] == ' ':
                output_string += s[i:j][::-1] + ' '
                i = j + 1
                j += 1
            j += 1
        output_string += s[i:j][::-1]
        return output_string
