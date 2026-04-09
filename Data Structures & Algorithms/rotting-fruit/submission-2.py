class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = [[0 for _ in range(COL)] for _ in range(ROW)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([])
        fresh = 0
        ans = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited[r][c] = True

        while q and fresh > 0:
            rotted = False
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            ans += 1

        return ans if not fresh else -1
                    
