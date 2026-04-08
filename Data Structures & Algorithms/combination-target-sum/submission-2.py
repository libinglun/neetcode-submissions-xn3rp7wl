class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(i):
            if sum(comb) == target:
                res.append(comb.copy())
                return
            elif sum(comb) > target:
                return 
            else:
                if i == len(nums):
                    return
                comb.append(nums[i])
                dfs(i)
                comb.pop()
                dfs(i + 1)

        dfs(0)
        return res


            