class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0' or visited[r][c]:
                return 
            visited[r][c] = True
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    ans += 1

        return ans