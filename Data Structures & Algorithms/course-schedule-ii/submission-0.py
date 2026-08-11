class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # initialise the DS for graph 
        graph = [[] for _ in range(numCourses)]
        total_nodes = numCourses

        # build the graph from edges. store as adj list
        # calculate the indegrees in the same loop
        indegrees = [0]*total_nodes
        for i in prerequisites:
            graph[i[1]].append(i[0]) # CAREFULL READ QUESTION DEPENDENCY FLOW FROM B- A [1,0] means to take 1 you need 0
            indegrees[i[0]]+=1

        from collections import deque
        q = deque()
        # push the nodes with 0 dependency into the queue
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(node)

        schedule = []
        while q:
            curr = q.popleft()
            schedule.append(curr)
            for adj in graph[curr]:
                indegrees[adj]-=1
                if indegrees[adj]==0:
                    q.append(adj)
        
        if len(schedule)==total_nodes:
            return schedule
        else:
            return []
        
        