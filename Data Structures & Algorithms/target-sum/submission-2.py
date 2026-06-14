class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Top-down DP:
        total_sum = sum(nums)
        offset = total_sum
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