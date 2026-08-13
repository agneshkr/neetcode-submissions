# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(p, q):
            # check equality
            if (p is None) and (q is None):
                return True
            elif (p is None) or (q is None):
                return False

            return all([
                p.val==q.val,
                dfs(p.left, q.left),
                dfs(p.right, q.right)
            ])
        return dfs(p, q)