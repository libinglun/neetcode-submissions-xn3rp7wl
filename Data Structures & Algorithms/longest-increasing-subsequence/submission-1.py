class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * n for _ in range(n)]
        def dfs(i, last):
            if i == len(nums):
                return 0

            if last != -1 and memo[i][last] != -1:
                return memo[i][last]

            LIS = dfs(i + 1, last)
            if last == -1 or nums[last] < nums[i]:
                LIS = max(LIS, dfs(i + 1, i) + 1)

            memo[i][last] = LIS
            return LIS

        return dfs(0, -1)

            