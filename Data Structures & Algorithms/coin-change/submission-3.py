class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top-down DP: dfs to search with memory array
        '''
        memo = [-1] * (amount + 1)
        def dfs(remain):
            if remain == 0:
                return 0

            if memo[remain] != -1:
                return memo[remain]

            res = 1e9
            for coin in coins:
                if remain >= coin:
                    res = min(res, 1 + dfs(remain - coin))

            memo[remain] = res
            return memo[remain]
        ans = dfs(amount)
        return -1 if ans == 1e9 else ans
        '''
        # Bottom-up DP
        # dp[i] represents the min. num. of coins to make up amount i
        # transition dp[i] = min(dp[i - c]) for c in coins
        dp = [1e9] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
    
        return dp[amount] if dp[amount] != 1e9 else -1

    
