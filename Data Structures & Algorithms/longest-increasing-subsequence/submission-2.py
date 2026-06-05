class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # memo = [[-1] * n for _ in range(n)]
        # def dfs(i, last):
        #     if i == len(nums):
        #         return 0

        #     if last != -1 and memo[i][last] != -1:
        #         return memo[i][last]

        #     LIS = dfs(i + 1, last)
        #     if last == -1 or nums[last] < nums[i]:
        #         LIS = max(LIS, dfs(i + 1, i) + 1)

        #     memo[i][last] = LIS
        #     return LIS

        # return dfs(0, -1)
        if not nums:
            return 0
        # Let dp[i] represents the LIS at index i
        dp = [1] * len(nums)

        # for each i, we look for every previous index j such that nums[i]>nums[j]
        # which means we can append i to LIS ends at j.
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # the last one is not necessarily the best one
        return max(dp)


            