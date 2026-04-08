# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # by BFS
        '''
        if not root:
            return 0
        max_depth = 0
        queue = [root]
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_depth += 1

        return max_depth
        '''
        # by recursive DFS
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        if not root:
            return 0
        return dfs(root)
