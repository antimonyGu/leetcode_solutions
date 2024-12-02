# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def leftdfs(node):
            if not node:
                return []

            # skip leave nodes
            if node.left == None and node.right == None:
                return []

            if node.left:
                return [node.val] + leftdfs(node.left)

            if node.right:
                return [node.val] + leftdfs(node.right)

        def findLeaves(node):
            if not node:
                return []
            
            if node.left == None and node.right == None:
                return [node.val]
            else:
                return findLeaves(node.left) + findLeaves(node.right)

        def rightdfs(node):
            if not node:
                return []

            # skip leave nodes
            if node.left == None and node.right == None:
                return []

            if node.right:
                return rightdfs(node.right) + [node.val]
            else:
                return rightdfs(node.left) + [node.val]
        
        leftandleavesandright = [root.val] + leftdfs(root.left) + findLeaves(root.left) + findLeaves(root.right) + rightdfs(root.right)
        return leftandleavesandright
