# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return float('-inf'), 0

            left_max_stop, left_max_continue = dfs(node.left)
            right_max_stop, right_max_continue = dfs(node.right)

            max_stop = max(left_max_continue + node.val + right_max_continue, left_max_stop, right_max_stop, node.val)
            max_continue = max(left_max_continue + node.val, right_max_continue + node.val, node.val)

            return max_stop, max_continue

        return max(dfs(root))


        