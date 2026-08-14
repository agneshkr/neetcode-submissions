# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        res, q = [], deque([root])

        if root is None:
            return []

        while q:
            
            curr = []
            for i in range(len(q)):
                curr_node = q.popleft()
                curr.append(curr_node.val)
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)           
            res.append(curr)
        return res
                

