class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Top-down DP:
        # states: 0 - buy 1 - sale 2 cooldown
        n = len(prices)
        '''
        def dfs(i, state):
            if i >= n:
                return 0

            next_state = 0 if state == 2 else state
            skip = dfs(i + 1, next_state)
            if state == 0:
                buy = dfs(i + 1, 1) - prices[i]
                return max(buy, skip)
            if state == 1:
                sale = dfs(i + 1, 2) + prices[i]
                return max(sale, skip)
            if state == 2:
                return skip

        return dfs(0, 0)
        '''
        # 2D-DP:
        # dp[i][0] = max profit from day i to end if we can BUY
        # dp[i][1] = max profit from day i to end if we can SELL
        dp = [[0] * 2 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] - prices[i])
            dp[i][1] = max(dp[i + 1][1], dp[i + 2][0] + prices[i])

        return dp[0][0]
