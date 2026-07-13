class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_count= 0 

        def dfs(r, c):
            

            if (
                (r<0 or r >= len(grid)) or 
                (c<0 or c >= len(grid[0])) or
                grid[r][c] == 0
            ):
                return 0
            grid[r][c] = 0
            return 1 + (
                dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            )


        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==1:
                    max_count = max(max_count, dfs(i, j))
        
        return max_count
        