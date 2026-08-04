class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            

            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return 0
            
            grid[r][c]=0
            area = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                area += dfs(nr, nc)
            
            return area

        min_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    min_area = max(min_area, dfs(i, j))
        return min_area
        