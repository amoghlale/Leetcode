class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Dynamic programming solution
        n, ans = len(s), [0, 0]

        # Create an n * n matrix initialized to false
        dp = [[False] * n for _ in range(n)]

        # single characters are palindromes, update [i][i] to True in dp
        for i in range(n):
            dp[i][i] = True

        # consecutive same characters are palindromes, update [i][i+1] to True in dp if they are same
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # slice value will be more than 2 till n
        # i will iterate from 0 to n - slice value
        # j will be upper limit of slice_value
        # if i = j, and [i+1][j-1] is True, i, j is a palindrome inclusive of i, j
        # update dp and ans
        for slice_val in range(2, n):
            for i in range(n - slice_val):
                j = i + slice_val
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]
        i, j = ans
        return s[i: j + 1]
