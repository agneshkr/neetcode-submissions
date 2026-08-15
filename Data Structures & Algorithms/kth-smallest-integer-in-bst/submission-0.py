# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:



        # def dfs(node):
        # start from left side which would have smallest.
        # need to do this in stack so data is easily accessible
        
        stack, curr = [], root
        count=0
        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left
            count = count+1
            curr = stack.pop()
            if count==k:
                return curr.val
            curr = curr.right

