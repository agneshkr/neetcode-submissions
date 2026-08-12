class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            # In tree no of edges should be exactly n-1
            # if the value is more then there is a cycle
            # if the value is less than n-1 then it is disconnected.
            return False

        # if we got till here we have n-1 nodes exactly.
        # so if this is not a graph that means one edge is used for this that was other wise used to
        # connect the whole nodes meaning it will be disconnected.
        # so either it's a graph and disconnected or it is a tree.
        # so by proving it's not disconnected we can prove this is a tree

        graph = [[] for _ in range(n)]
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        visited = set()
        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)     
            return True   
        
        dfs(0)

        return len(visited)==n