class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = (
            (-1, 0), (1, 0),
            (0, -1), (0, 1)
        )
        visited = set()
        from collections import deque
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    visited.add((r,c))
                    q.append((r,c))
        def is_all_rotten():
            fresh_available = False         
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        fresh_available=True
            return (not fresh_available)
        time = 0
        while q:
            if is_all_rotten():
                break
            # print(time, q, grid)
            for i in range(len(q)):
                r, c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and 0 <= nc < cols \
                        and (nr, nc) not in visited \
                        and grid[nr][nc]==1 
                    ):
                        grid[nr][nc]=2
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))
            time+=1
        
        if not is_all_rotten():
            return -1
        return time