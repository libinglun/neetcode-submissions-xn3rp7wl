class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dfs to search with memory array
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