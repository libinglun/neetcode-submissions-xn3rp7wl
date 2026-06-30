class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Top-down DP:
        memory = [[-1] * col for _ in range(row)]
        def dfs(i, j, preval):
            if i < 0 or j < 0 or i >= row or j >= col or preval >= matrix[i][j]:
                return 0

            if memory[i][j] != -1:
                return memory[i][j]
            
            res = 1
            for di, dj in directions:
                res = max(res, 1 + dfs(i + di, j + dj, matrix[i][j]))
                
            memory[i][j] = res
            return res

        ans = 0
        for r in range(row):
            for c in range(col):
                ans = max(ans, dfs(r, c, -1))

        return ans
