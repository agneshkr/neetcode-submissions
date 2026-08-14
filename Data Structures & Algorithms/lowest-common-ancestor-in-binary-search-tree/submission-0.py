# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        
        s,l = (p, q) if (p.val<q.val) else (q, p)
        def dfs(node):

            if node is None:
                return
            
            if s.val <= node.val <= l.val:
                return node
            elif l.val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        lca = dfs(root)
        return lca