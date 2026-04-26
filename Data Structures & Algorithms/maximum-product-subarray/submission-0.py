class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] represents the max product in nums[:i]
        cur_min = 1
        cur_max = 1
        res = nums[0]

        for num in nums:
            tmp = cur_max
            # first two continues, third stop
            cur_max = max(num * cur_max, num * cur_min, num)
            # even if cur_min is positive is fine
            cur_min = min(num * tmp, num * cur_min, num)
            res = max(res, cur_max)

        return res