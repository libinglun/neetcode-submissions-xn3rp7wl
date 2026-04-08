"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old2new = {}
        old2new[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            newn = Node(cur.val)
            for nb in cur.neighbors:
                if nb not in old2new:
                    old2new[nb] = Node(nb.val)
                    q.append(nb)

                old2new[cur].neighbors.append(old2new[nb])

        return old2new[node]
            
        