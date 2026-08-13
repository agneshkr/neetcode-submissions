# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def sub(p, q):
            # check subtree assume q is the sub tree
            if (p is None) and (q is None):
                return True
            elif (p is None) and (q is not None):
                return False
            elif (q is None) and (p is not None):
                return False

            return all([
                p.val==q.val,
                sub(p.left, q.left),
                sub(p.right, q.right)
            ])
        present = False
        def dfs(node):
            nonlocal present
            if node is None:
                return
            print('node', node.val)
            if node.val == subRoot.val:
                
                present = sub(node, subRoot)
                print('here', node.val, present)
                if present:
                    return
            if not present:
                dfs(node.left)
            if not present:
                dfs(node.right)
        dfs(root)
        return present
