class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(nums):
            if sum(comb) == target:
                res.append(comb.copy())
                return
            elif sum(comb) > target:
                return 
            else:
                if not nums:
                    return
                comb.append(nums[0])
                dfs(nums)
                comb.pop()
                dfs(nums[1:])

        dfs(nums)
        return res


            