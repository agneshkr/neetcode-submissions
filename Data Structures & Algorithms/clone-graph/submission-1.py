"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        results = []

        visited= {}
        def bfs(node):

            if node is None:
                return None
            
            if node in visited:
                return visited[node]

            clone = Node(node.val)
            clone.neighbors = []
            visited[node] = clone

            for i in node.neighbors:
                clone.neighbors.append(bfs(i))
            return clone

        return bfs(node)
        
        