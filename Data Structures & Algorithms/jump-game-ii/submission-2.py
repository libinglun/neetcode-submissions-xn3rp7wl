class Solution:
    def jump(self, nums: List[int]) -> int:
        # Top-down DP:
        '''
        memory = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums) - 1:
                return 0

            if i < len(nums) and memory[i] != -1:
                return memory[i]

            # try later index for early exists.
            ans = 1e9
            for j in range(nums[i], 0, -1):
                ans = min(dfs(i + j) + 1, ans)

            memory[i] = ans
            return memory[i]

        return dfs(0)
        '''
        # Greedy: for each jump we have a range
        # every time we figure out the farthest point we can jump from this range
        farthest = 0
        ans = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            ans += 1

        return ans

