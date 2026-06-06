class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D dp: dp[i][j] represents the LCS of text1[:i] and text2[:j]
        # dp[i][j] = dp[i - 1][j - 1] + 1 if text1[i] == text2[j] else max(dp[i - 1][j], dp[i][j - 1])
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diag = -1
                if text1[i - 1] == text2[j - 1]:
                    diag = dp[i - 1][j - 1] + 1
                dp[i][j] = max(diag, dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

