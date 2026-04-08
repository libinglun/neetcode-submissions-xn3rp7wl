# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)

        right_length = len(inorder[index+1:])
        left_length = len(inorder) - 1 - right_length

        # build left subtree
        left = self.buildTree(preorder[1:left_length+1], inorder[:index])

        # build right subtree
        right = self.buildTree(preorder[left_length+1:], inorder[index+1:])

        root.left = left
        root.right = right

        return root