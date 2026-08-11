from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            start, end = pre[0], pre[1]
            graph[start].append(end)
        
        indegrees = [0]*numCourses
        # caculate the in-degrees
        for node in range(numCourses):
            for adj_node in graph[node]:
                indegrees[adj_node] += 1

        q = deque()
        # keep the nodes with 0-indegree in a queue
        # these are the nodes with zero dependency.
        # we can add this to the stack first.
        for node, degree in enumerate(indegrees):
            if degree==0:
                q.append(node)
        
        res=[]
        while q:
            node = q.popleft()
            res.append(node)
            for adj in graph[node]:
                indegrees[adj]-=1
                if indegrees[adj]==0:
                    q.append(adj)
        for i in indegrees:
            if i!=0:
                return False
        return True
            



    