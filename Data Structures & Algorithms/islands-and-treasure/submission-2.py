class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==INF:
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr, nc))
        