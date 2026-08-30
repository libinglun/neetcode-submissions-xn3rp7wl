class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # i >> 1 divides i by 2 (shifts off the rightmost bit)
            # i & 1 checks if the rightmost bit is 1 (i.e., if i is odd)
            dp[i] = dp[i >> 1] + (i & 1)

        return dp