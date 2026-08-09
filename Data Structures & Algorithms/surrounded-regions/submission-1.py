from collections import deque

class Solution:

    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        check_list = []
        grid=board
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if (r==0 or r== rows-1 or c==0 or c==cols-1) and grid[r][c]=="O":
                    check_list.append((r,c))
                    visited[r][c]=1

        
        def dfs(r, c):

            for dr, dc in self.DIRECTIONS:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="O" and visited[nr][nc]!=1:
                    visited[nr][nc]=1
                    dfs(nr, nc)
        for r,c in check_list:
            dfs(r,c)
        # print(visited)
        for i in range(rows):
            for j in range(cols):
                # print(grid[i][j]=="O", visited[r][c]==0)
                if grid[i][j]=="O" and visited[i][j]==0:
                    grid[i][j]="X"


        