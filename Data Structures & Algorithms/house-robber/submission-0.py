class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_rob = [0] * n
        dp_not = [0] * n

        dp_rob[0] = nums[0]
        for i in range(1, n):
            dp_rob[i] = dp_not[i - 1] + nums[i]
            dp_not[i] = max(dp_rob[i - 1], dp_not[i - 1])

        return max(dp_rob[-1], dp_not[-1])