class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def dfs(x, y):
            

            if 0<=x<rows and 0<=y<cols:
                # print(x, y, grid, grid[x], grid[x][j])
                if grid[x][y] == 1:
                    grid[x][y]=0
                    # print(f'({x}, {j}) marked to 0')
                    count = 1+dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)
                    # print()
                    return count
                else:
                    return 0
            # else:
            #     print(x, y, 'skipped') 

            return 0
        maxarea=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    currArea = dfs(i,j)
                    print('curr', currArea)
                    maxarea = max(currArea, maxarea)
        return maxarea
        