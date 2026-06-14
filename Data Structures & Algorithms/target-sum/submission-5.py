class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Top-down DP:
        total_sum = sum(nums)
        offset = total_sum
        '''
        memo = [[-1] * (2 * total_sum + 1) for _ in range(len(nums))]
        def dfs(i, nsum):
            if i == len(nums):
                return nsum == target
            if memo[i][nsum + offset] != -1:
                return memo[i][nsum + offset]

            res = 0
            res += dfs(i + 1, nsum + nums[i])
            res += dfs(i + 1, nsum - nums[i])
            memo[i][nsum + offset] = res
            return memo[i][nsum + offset]
  
        return dfs(0, 0)
        '''
        # Bottom-up DP: dp[i] represents the number of ways to get sum i
        '''
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]
        '''
        # Space optimised
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(n):
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + nums[i]] += count
                next_dp[total - nums[i]] += count
            dp = next_dp

        return dp[target]
