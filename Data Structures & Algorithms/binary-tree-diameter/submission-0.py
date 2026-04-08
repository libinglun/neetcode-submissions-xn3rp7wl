# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # Use an instance variable to track the maximum diameter
        
        def height(node):
            if not node:
                return 0
            
            lefth = height(node.left)
            righth = height(node.right)
            
            # Update the global maximum diameter found so far
            self.ans = max(self.ans, lefth + righth)
            
            return max(lefth, righth) + 1

        height(root)
        return self.ans

        

        
