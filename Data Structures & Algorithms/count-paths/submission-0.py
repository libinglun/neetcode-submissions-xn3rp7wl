class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2D DP: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp = [[0] * (n + 2) for _ in range(m + 2)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        print(dp)

        
        return dp[m][n]
