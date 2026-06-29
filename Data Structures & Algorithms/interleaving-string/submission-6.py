class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Top-down DP:
        '''
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(str1, str2, target):
            if target == "":
                return True

            if (str1, str2) in dp:
                return dp[(str1, str2)]

            tmp1 = False
            tmp2 = False
            if str1 and str1[0] == target[0]:
                tmp1 = dfs(str1[1:], str2, target[1:])
            
            if str2 and str2[0] == target[0]:
                tmp2 = dfs(str1, str2[1:], target[1:])

            dp[(str1, str2)] = tmp1 or tmp2
            return dp[(str1, str2)]

        return dfs(s1, s2, s3)
        '''
        # Bottom-up DP: dp[i][j] represents whether it can form s3[i + j] or not
        '''
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True

                if j > 0 and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[len(s1)][len(s2)]
        '''
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            next_dp = [False] * (len(s2) + 1)
            next_dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(len(s2) + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and dp[j]:
                    next_dp[j] = True

                if j > 0 and s2[j - 1] == s3[i + j - 1] and next_dp[j - 1]:
                    next_dp[j] = True

            dp = next_dp

        return dp[len(s2)]
