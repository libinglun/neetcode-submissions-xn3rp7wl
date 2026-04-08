class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        comb = []
        def dfs(i):
            if sum(comb) == target:
                res.append(comb.copy())
                return 
            if sum(comb) > target or i >= len(candidates):
                return 
            
            comb.append(candidates[i])
            print(comb)
            dfs(i + 1)
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res