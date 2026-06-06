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


