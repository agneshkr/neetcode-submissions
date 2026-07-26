class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        
        def dfs(x, y):


            if 0<=x<rows and 0 <=y<cols and grid[x][y]=="1":
                grid[x][y] = "0"
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
            else:
                return

        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    count=count+1
                    dfs(i, j)
        return count
        