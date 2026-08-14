# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        
        if root is None:
            return []
        res, q = [], deque([root])
    
        while q:

            curr = []
            for i in range(len(q)):
                curr_node = q.popleft()
                curr.append(curr_node.val)
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            res.append(curr[-1])

        return res