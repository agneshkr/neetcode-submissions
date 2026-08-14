# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def dfs(node, path_max):
            nonlocal count
            if node is None:
                return None

            if node.val >= path_max:
                path_max = node.val
                # res.append(node.val)
                count+=1

            dfs(node.left, path_max)
            dfs(node.right, path_max)
        
        dfs(root, root.val)
        return count
