class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] reprents the larget sum of ending at index i
        # dp[i + 1] = max(nums[i], dp[i] + nums[i])
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)