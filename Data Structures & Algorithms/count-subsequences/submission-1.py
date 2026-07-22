class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Top-down DP:
        '''
        memory = [ [-1] * (len(t) + 1) for _ in range(len(s) + 1)]
        def dfs(s, t):
            if len(t) == 0:
                return 1

            if len(s) == 0:
                return 0

            if memory[len(s)][len(t)] != -1:
                return memory[len(s)][len(t)]

            skip = dfs(s[1:], t)
            ans = 0
            if s[0] == t[0]:
                ans = dfs(s[1:], t[1:]) + skip
            else:
                ans = skip
            memory[len(s)][len(t)] = ans
            return ans

        return dfs(s, t)
        '''
        # Bottom-up DP:
        # dp[i][j] represents all distinct subsequences of s[i:] and t[j:]
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1
    
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]
