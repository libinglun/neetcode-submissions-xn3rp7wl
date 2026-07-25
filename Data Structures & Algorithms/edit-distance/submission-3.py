class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Top-down DP:
        '''
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = dfs(i + 1, j + 1)
                return dp[i][j]

            insert = dfs(i, j + 1) + 1
            delete = dfs(i + 1, j) + 1
            replace = dfs(i + 1, j + 1) + 1

            dp[i][j] = min(insert, delete, replace)

            return dp[i][j]

        return dfs(0, 0)
        '''

        # Bottom-up DP:
        # dp[i][j] represents the edit distance from word1[:i + 1] to word2[:j + 1]
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],  # Delete from word1
                        dp[i][j - 1],  # Insert into word1
                        dp[i - 1][j - 1],  # Replace
                    )

        return dp[m][n]


            