# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])

        # level traverse
        while q[0] is not None:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)

        # pop all None in q
        while q and q[0] is None:
            q.popleft()
        
        # check whether q is empty
        return not any(q)