# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(lambda: [])

        def dfs(node, col, row):
            if not node: return
            mp[col].append((row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        
        result = []
        for col in sorted(mp.keys()):
            mp[col].sort()
            result.append([val for _, val in mp[col]])
        
        return result