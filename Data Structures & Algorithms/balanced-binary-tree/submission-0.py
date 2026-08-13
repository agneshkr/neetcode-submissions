# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def max_height(node):
            if not node:
                return 0
            # return height
            return 1+max(max_height(node.left), max_height(node.right))
        

        def is_balanced(node):

            if not node:
                return True

            return all([
                abs(max_height(node.left)-max_height(node.right))<=1,
                is_balanced(node.left),
                is_balanced(node.right)]
            )
        
        return is_balanced(root)