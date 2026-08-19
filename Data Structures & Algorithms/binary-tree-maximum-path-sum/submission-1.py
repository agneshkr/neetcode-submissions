# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')

        def dfs(node):
            nonlocal best
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            best = max(best, node.val + max(r, 0) + max(l, 0))
            return node.val + max(l, r, 0)
        dfs(root)

        return best
        