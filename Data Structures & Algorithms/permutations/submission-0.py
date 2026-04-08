class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, idx):
            if idx == len(nums):
                res.append(nums[:])
                return 
            print(idx)
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                print(nums[0: idx+1], nums[idx+1:])
                dfs(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        dfs(nums, 0)

        return res
                