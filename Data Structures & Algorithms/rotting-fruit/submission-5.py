class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh_count=fresh_count+1
                

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        time=0
        if not q:
            if fresh_count>0:
                return -1
            else:
                return 0
        while q:
            prev_fresh_count = fresh_count
            for i in range(len(q)):
                cr, cc = q.popleft()
                for dr,dc in directions:
                    nr, nc = cr+dr, cc+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        neigh_val = grid[nr][nc]
                        if neigh_val==1:
                            grid[nr][nc]=0
                            print(nr, nc)
                            fresh_count=fresh_count-1
                            q.append((nr, nc))
            print(fresh_count, prev_fresh_count)
            if prev_fresh_count==fresh_count:
                
                if fresh_count>0:
                    return -1    
                return time
            time=time+1
        return time
        