class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Top-down DP:
        '''
        memo = [[-1] * (amount + 1) for _ in range(len(coins))] 
        def dfs(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            res = 0
            # combination
            if amount >= coins[i]:
                res += dfs(i, amount - coins[i])
            res += dfs(i + 1, amount)

            memo[i][amount] = res
            return memo[i][amount]

        return dfs(0, amount)
        '''
        ### Bottom-up DP
        # dp[i] represents the number of dict comb that total up to amount i
        # transition: 
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(amount + 1): 
                if i >= c:
                    dp[i] += dp[i - c]

        return dp[amount]



        