class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = [[0 for _ in range(col)] for _ in range(row)]

        max_area = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or not grid[r][c] or visited[r][c]:
                return 0
            visited[r][c] = 1
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1) 

        for r in range(row):
            for c in range(col):
                if grid[r][c] and not visited[r][c]:
                    max_area = max(max_area, dfs(r, c))

        return max_area