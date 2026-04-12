class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(len(edges) + 1)]
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        cycle = set()
        def dfs(node, parent):
            if node in visited:
                cycle.add(node)
                return False

            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    if node in cycle:
                        return True
                    cycle.add(node)
                    return False

            return True

        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return [] 
        