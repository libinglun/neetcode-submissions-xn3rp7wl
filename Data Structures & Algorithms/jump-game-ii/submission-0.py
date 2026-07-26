class Solution:
    def jump(self, nums: List[int]) -> int:
        # Top-down DP:
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