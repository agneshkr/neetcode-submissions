class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count=0

        row_len = len(grid)
        column_len = len(grid[0])
        def dfs(row, column):
            # only used for marking visited nodes.
            # print("INSIDE DFS")
            if (row<0 or row >= row_len) or (column<0 or column >= column_len) or (grid[row][column]=="0"):
                return
            
            print('RC', row, column)
            grid[row][column] = "0" # basically mark it as visited.

            dfs(row+1, column)
            dfs(row-1, column)
            dfs(row, column+1)
            dfs(row, column-1)

            return
        print('RUNNING')
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if grid[r][c] == '1':
                    count+=1
                    dfs(r,c)

        return count


    
        