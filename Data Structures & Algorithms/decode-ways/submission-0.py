class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] represents the number of ways to decode s[i:]
        # dp[i + 1] = dp[i] + dp[i - 1] if s[i:i+2] can be decoded

        n = len(s)
        dp = [1] * (n + 1)

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]

        return dp[0]