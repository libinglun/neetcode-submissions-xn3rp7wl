# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BINARY SEARCH TREE!
        print(root.val)
        if root is None:
            return None
        
        # WLOG assume p < q:
        if p.val > q.val:
            p, q = q, p

        if p.val < root.val and root.val < q.val:
            return root
        elif p.val == root.val:
            return p
        elif q.val == root.val:
            return q
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        
        
        
        
        
        # brute force
        '''
        # DFS to find p and q and record their paths
        self.p_path = None
        self.q_path = None
        self.p = p
        self.q = q

        def dfs(node, path):
            for n in path:
                print(n.val, end=' ')
            print()
            if node.val == self.p.val:
                self.p_path = path.copy()
            if node.val == self.q.val:
                self.q_path = path.copy()
            if node.left:
                path.append(node.left)
                dfs(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right)
                dfs(node.right, path)
                path.pop()
            return 

        dfs(root, [root])

        # compare the path to find the common value with the highest index
        hashset = set(self.p_path)
        for i in range(len(self.q_path) - 1, -1, -1):
            if self.q_path[i] in hashset:
                return self.q_path[i]
        '''


