class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            dfs(i + 1)
            val = subset.pop()
            i += 1
            while i < len(nums) and val == nums[i]:
                i += 1
            dfs(i)

        dfs(0)
        return res
            