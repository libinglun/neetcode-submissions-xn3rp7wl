class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Top-down DP:
        dp = [[-1] * (len(word2)) for _ in range(len(word1))]
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if dp[i][j] != -1:
                return dp[i][j]

            match = 1e9
            if word1[i] == word2[j]:
                match = dfs(i + 1, j + 1)

            insert = dfs(i, j + 1) + 1
            delete = dfs(i + 1, j) + 1
            replace = dfs(i + 1, j + 1) + 1

            dp[i][j] = min(insert, delete, replace, match)

            return dp[i][j]

        return dfs(0, 0)


            