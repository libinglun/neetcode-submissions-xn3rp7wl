class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums) // 2
        n = len(nums)
        # find the elements that can constitute a half
        # can use dfs to search
        # this has time complexity O(2^n)
        '''
        def dfs(i, total):
            if total == half:
                return True
            
            if i >= len(nums) or total > half:
                return False

            return dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

        return dfs(0, 0)
        '''
        # can be improved by using a memory array
        # use a 2D array to record whether a value can reached
        # this has both time and space complextiy O(n * half)
        '''
        memo = [[-1] * (half + 1) for _ in range(n + 1)]
        def dfs(i, total):
            if total == half:
                return True
            
            if i >= len(nums) or total > half:
                return False

            if memo[i][total] != -1:
                return memo[i][total]

            memo[i][total] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)
            return memo[i][total]

        return dfs(0, 0)
        '''
        # bottom-up DP: dp[i][j] represents can we use first i items to form sum j?
        # base cases: dp[i][0]
        '''
        dp = [[False] * (half + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, half + 1):
                if nums[i - 1] <= j:
                    # we can the jth element or we don't
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    # we can't take it
                    dp[i][j] = dp[i - 1][j]

        return dp[n][half]
        '''
        # bottom-up DP: dp[j] represents sum j can be achieved using numbers so far
        dp = [False] * (half + 1)
        dp[0] = True
        for num in nums:
            # Loop backwards to prevent using the same number twice
            for j in range(half, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[half]


