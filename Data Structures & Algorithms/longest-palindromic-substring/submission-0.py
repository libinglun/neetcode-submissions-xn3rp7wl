class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = True when s[i:j] is a palindrome
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        res_len = 0
        res_idx = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    
                    if res_len < (j - i + 1):
                        res_idx = i
                        res_len = j - i + 1

        return s[res_idx: res_idx + res_len]

