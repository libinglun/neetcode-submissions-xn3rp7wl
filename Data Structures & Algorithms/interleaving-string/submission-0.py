class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Top-down DP:
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