class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memory = [-1] * len(nums)
        def dfs(i):
            if i == len(nums) - 1:
                return True

            if i >= len(nums):
                return False

            if memory[i] != -1:
                return memory[i]

            if nums[i] == 0:
                return False

            for j in range(nums[i], 0, -1):
                if dfs(i + j):
                    memory[i] = True
                    return True

            memory[i] = False
            return memory[i]

        return dfs(0)