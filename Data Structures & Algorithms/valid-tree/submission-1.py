class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # A valid tree is a acyclic connected graph that contains n - 1 edges
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # Detect cycles in the tree
        visited = set()
        # Undirect edge --> pass parent to avoid loop back directly
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False

            return True

        # Check connectivity
        ans = dfs(0, 0)
        print(visited)
        print(ans, len(visited))
        if ans and len(visited) == n:
            return True
        return False

            

