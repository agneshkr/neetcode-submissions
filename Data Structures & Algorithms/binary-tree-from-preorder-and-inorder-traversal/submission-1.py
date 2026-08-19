# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

#         def build(preorder, inorder):
#             if not preorder:
#                 return None

#             root = TreeNode(preorder[0])
#             mid = inorder.index(preorder[0])
#             root.left = build(preorder[1:mid+1], inorder[:mid])
#             root.right = build(preorder[mid+1:], inorder[mid+1:])
#             return root
#         return build(preorder, inorder)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i,v in enumerate(inorder)}
        i = 0
        def build(lo, hi):
            nonlocal i
            if lo>hi:
                return None

            root = TreeNode(preorder[i])
            mid = idx[preorder[i]]
            i=i+1


            root.left = build(lo, mid-1)
            root.right = build(mid+1, hi)
            return root

        return build(0, len(inorder)-1)
    
        
        

        