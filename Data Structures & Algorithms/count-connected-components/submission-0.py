class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

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
        count=0
        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node)
        return count