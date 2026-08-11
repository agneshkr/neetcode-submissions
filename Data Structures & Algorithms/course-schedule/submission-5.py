from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        
        # 1. Build graph AND in-degrees in a single pass
        for start, end in prerequisites:
            graph[start].append(end)
            indegrees[end] += 1

        # 2. Initialize queue with 0-dependency nodes
        q = deque()
        for node, degree in enumerate(indegrees):
            if degree == 0:
                q.append(node)
        
        # 3. Track how many nodes we successfully process
        processed_count = 0
        
        while q:
            node = q.popleft()
            processed_count += 1
            
            for adj in graph[node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    q.append(adj)
                    
        # 4. If we processed all courses, there was no cycle.
        return processed_count == numCourses