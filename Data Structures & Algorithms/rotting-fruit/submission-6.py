class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = ((-1,0), (1, 0), (0, -1), (0, 1))
        from collections import deque
        q = deque()

        fresh=0 # maintain the number of fresh fruits.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r, c))
                elif grid[r][c]==1:
                    fresh=fresh+1
        elapsed_time = 0
        while q:
            if fresh==0:
                break
            elapsed_time=elapsed_time+1
            for i in range(len(q)):
                cr, cc = q.popleft()

                for dr, dc in directions:
                    nr, nc = cr+dr, cc+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh=fresh-1
        
        if fresh > 0:
            return -1
        
        return elapsed_time

