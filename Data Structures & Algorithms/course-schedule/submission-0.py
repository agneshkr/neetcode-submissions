class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i:[] for i in range(numCourses)}

        for i in prerequisites:
            graph[i[0]].append(i[1])
        state = {} # 0 for unvisited, 1 for visiting and 2 already visited and processed

        def dfs(idx):
            # detecting cycle return false
            if state.get(idx, 0)==1:
                return False # this is a cycle
            elif state.get(idx, 0)==2:
                return True


            state[idx] = 1
            for i in graph[idx]:
                if not dfs(i):
                    return False
            state[idx] = 2

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        
