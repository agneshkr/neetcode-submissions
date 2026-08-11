class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(numCourses)]
        for i in prerequisites:
            graph[i[1]].append(i[0])

        state = [0]*numCourses
        schedule = []
        def dfs(node):
            # cycle means True
            if state[node]==1: # cycle present current iteration reaches back to the processed node
                return True
            elif state[node]==2:
                # this was processed earlier and we found no cycles
                return False
            else:

                state[node]=1
                for adj in graph[node]:
                    if dfs(adj):
                        return True
                
                state[node]=2 # marked to processed no cycles found
                schedule.append(node)

        for i in range(numCourses):
            if state[i]==0 and dfs(i):
                return []

        return schedule[::-1]
        