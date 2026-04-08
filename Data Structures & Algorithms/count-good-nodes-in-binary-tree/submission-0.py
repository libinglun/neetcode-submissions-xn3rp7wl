# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS to find good node
        self.ans = 0
        def dfs(node, path):
            print([node.val for node in path])
            if not node:
                return 
            if node.val >= max([node.val for node in path]):
                self.ans += 1
            if node.left:
                path.append(node.left)
                dfs(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right)
                dfs(node.right, path)
                path.pop()

        dfs(root, [root])
        return self.ans
