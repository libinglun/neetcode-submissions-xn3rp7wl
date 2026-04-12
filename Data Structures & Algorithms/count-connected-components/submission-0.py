class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        ans = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                ans += 1

        return ans