class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Instead of deciding which balloon to pop first,
        # decide which balloon to pop LAST in a given range.
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] represents the maximum score we can get by popping i + i to j - 1
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(0, n - length):
                j = i + length
                
                for k in range(i + 1, j):
                    coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    if coins > dp[i][j]:
                        dp[i][j] = coins

        return dp[0][n - 1]