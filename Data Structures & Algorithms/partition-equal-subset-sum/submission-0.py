class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums) // 2
        # find the elements that can constitute a half
        # can use dfs to search
        # 
        def dfs(i, total):
            if total == half:
                return True
            
            if i >= len(nums) or total > half:
                return False

            return dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

        return dfs(0, 0)

