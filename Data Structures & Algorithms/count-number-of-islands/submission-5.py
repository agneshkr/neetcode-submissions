class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])


        def dfs(r, c):

            if r>=rows or r<0 or c>=cols or c<0 or grid[r][c]=="0":
                return
            
            grid[r][c] = "0"
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)

        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    count=count+1
                    dfs(i, j)
        
        return count
        