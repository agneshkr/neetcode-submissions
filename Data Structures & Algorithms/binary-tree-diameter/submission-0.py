# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        max_val = 0
        def max_height(node):
            # return height
            if not node:
                return 0

            return 1+max(max_height(node.left), max_height(node.right))

        def max_diameter(node):

            if not node:
                return 0
            
            curr_diameter = max_height(node.left) + max_height(node.right)

            return max(
                max_diameter(node.left),
                max_diameter(node.right),
                curr_diameter
            )

        




        return max_diameter(root)
        