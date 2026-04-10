class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        visited1 = [[0 for _ in range(col)] for _ in range(row)]
        visited2 = [[0 for _ in range(col)] for _ in range(row)]

        q_pacific = deque([])
        q_atlantic = deque([])

        ans = []

        for c in range(col):
            q_pacific.append((0, c))
            visited1[0][c] = 1
            q_atlantic.append((row-1, c))
            visited2[row-1][c] = 1

        for r in range(row):
            q_pacific.append((r, 0))
            visited1[r][0] = 1
            q_atlantic.append((r, col-1))
            visited2[r][col-1] = 1

        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))

        bfs(q_pacific, visited1)
        bfs(q_atlantic, visited2)

        for r in range(row):
            for c in range(col):
                if visited1[r][c] and visited2[r][c]:
                    ans.append((r, c))

        return ans


        