class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        
        # create adjacency list to represent the graph
        graph = {i:[] for i in range(numCourses)}
        for pre in prerequisites:
            edge_start, edge_end = pre[0], pre[1]
            graph[edge_start].append(edge_end)


        state = [0]*len(graph) # 0-unvisited, 1-visited, 2-visiting
        def dfs(node):
            # return True if there is cycle
            if state[node]==2:
                return True
                # we have encountered this node before in this dfs iteration
                # this means there is a cycle return True
            elif state[node]==1:
                # if we find a cycle in a dfs traversal we exit immediately.
                # so the fact that you got here and the node is already visisted means
                # we did not encounter an cycle last time we traversed through this node.
                # so we can confidently return False indicating no cycle
                return False
            else:

                state[node]=2 # mark the node as visiting and traverse rest
                for adj in graph[node]:
                    if dfs(adj):
                        return True
                state[node]=1 # mark it as visited so next time when we reach here we can easily conclude that there 
                # are no cycles without further iterations.

                return False # the fact that you cheached here means there are no cycles 
                # --> we checked all the routes from this node
        
        # traverse starting from all nodes and check for cycles
        for i in graph.keys():
            if dfs(i):
                # there is a cycle
                # so this course schedule is not possible
                return False
        return True
        

        

        
        