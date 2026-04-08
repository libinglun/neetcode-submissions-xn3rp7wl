# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        # in order traversal of BST
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            
            self.k -= 1
            if self.k == 0:
                self.ans = node.val

            traverse(node.right)

        traverse(root)
        return self.ans
