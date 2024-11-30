# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def exists(root, node):
            if not root:
                return False
            
            if root == node:
                return True
            
            return exists(root.left, node) or exists(root.right, node)

        def LCA(root, p, q):
            if not root or root == p or root == q:
                return root

            l = LCA(root.left, p, q)
            r = LCA(root.right, p, q)

            if l and r:
                return root

            return l or r

        if not exists(root, p) or not exists(root, q):
            return None
        
        return LCA(root, p, q)