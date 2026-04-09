class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROW = len(grid)
        COL = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(row, col):
            q = deque([(row, col)])
            visited = [[0 for _ in range(COL)] for _ in range(ROW)]
            visited[row][col] = True
            dist = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return dist
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < ROW and 0 <= nc < COL and
                            not visited[nr][nc] and grid[nr][nc] != -1
                        ):
                            visited[nr][nc] = True
                            q.append((nr, nc))

                dist += 1

            return INF

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
                


        # DFS (backtracking) is inefficient to find the shortest path
        # visited = [[0 for _ in range(COL)] for _ in range(ROW)]
        # calculated = [[0 for _ in range(COL)] for _ in range(ROW)]
        # def dfs(r, c):
        #     if r < 0 or c < 0 or r == ROW or c == COL or grid[r][c] == -1 or visited[r][c]:
        #         return INF
           
        #     if grid[r][c] == 0:
        #         return 0

        #     if calculated[r][c]:
        #         return grid[r][c]

        #     visited[r][c] = True
        #     res = 1 + min(dfs(r + 1, c), 
        #                 dfs(r - 1, c),
        #                 dfs(r, c + 1), 
        #                 dfs(r, c - 1))
            
        #     visited[r][c] = False
        #     return res

        # for r in range(ROW):
        #     for c in range(COL):
        #         if grid[r][c] == INF:
        #             grid[r][c] = dfs(r, c)
        #             calculated[r][c] = True
                    

        # return