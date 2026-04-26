class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] represents the min num of coints to make up i
        # dp[i] = min(dp[i], 1 + dp[i - c]) for c in coins
        INF = float("inf")
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != INF else -1