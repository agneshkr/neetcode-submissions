# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i,v in enumerate(inorder)}
        i=0

        def build(lo, hi):
            nonlocal i
            if lo>hi: # this is that edge case handling
                return None

            curr = preorder[i]
            node = TreeNode(curr)
            mid = idx[curr]
            i+=1
            node.left = build(lo, mid-1)  # when lo==high --> no left node present call is made
            node.right = build(mid+1, hi) # at this point lo=high --> no right node is present need to handle this

            return node

        return build(0, len(inorder)-1)    

