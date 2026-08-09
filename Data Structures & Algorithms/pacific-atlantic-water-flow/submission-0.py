from collections import deque

class Solution:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pacific = deque()
        atlantic = deque()
        # pacific = []
        # atlantic = []
        grid = [[[] for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0:
                    pacific.append((r, c))
                    grid[r][c].append('p')
                if r==rows-1 or c==cols-1:
                    atlantic.append((r, c)) 
                    grid[r][c].append('a')
        
        while pacific:
            cr, cc = pacific.popleft()
            for dr, dc in self.DIRECTIONS:
                nr, nc = cr+dr, cc+dc
                if 0<=nr<rows and 0<=nc<cols and heights[cr][cc]<=heights[nr][nc] and 'p' not in grid[nr][nc]:
                    grid[nr][nc].append('p')
                    pacific.append((nr, nc))
        
        while atlantic:
            cr, cc = atlantic.popleft()
            for dr, dc in self.DIRECTIONS:
                nr, nc = cr+dr, cc+dc
                if 0<=nr<rows and 0<=nc<cols and heights[cr][cc]<=heights[nr][nc] and 'a' not in grid[nr][nc]:
                    grid[nr][nc].append('a')
                    atlantic.append((nr, nc))
        results = []
        for r in range(rows):
            for c in range(cols):
                if 'a' in grid[r][c] and 'p' in grid[r][c]:
                    results.append([r,c])
        return results

        