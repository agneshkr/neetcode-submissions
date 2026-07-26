class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        rows, cols = len(grid), len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    # dist = 0
                    q.append((i,j))
        
        while q:
            cr, cc = q.popleft()
            for dr, dc in directions:
                nr, nc = cr+dr, cc + dc
                if 0<=nr<rows and 0<=nc<cols:
                    curr_val = grid[nr][nc]
                    if curr_val == INF:
                        grid[nr][nc] = grid[cr][cc]+1
                        q.append((nr, nc))
        # return grid