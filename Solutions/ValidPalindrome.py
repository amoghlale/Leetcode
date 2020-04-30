class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphabets = ''.join([i.lower() for i in s if i.isalnum()])
        return True if alphabets[:] == alphabets[::-1] else False
