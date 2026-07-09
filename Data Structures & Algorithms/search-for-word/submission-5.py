class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def explore(x, y, curr, visited):
            
            satisfies = False
            def range(x, y):
                return 0 <= x < len(board) and 0 <= y < len(board[0])
            curr = curr+board[x][y]
            if len(curr) > len(word):
                return False
            # print('--->', x,y, curr)
            # if curr=='cdb':
                # print(visited)
            if curr == word:
                # print(x, y, word)
                return True

            
            visited.append((x,y))
            for x1, y1 in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if range(x1,y1) and ((x1,y1) not in visited) and (curr.startswith(word) or word.startswith(curr)):
                    # print('PREV', visited, visited != (x1,y1))
                    satisfies = satisfies or explore(x1, y1, curr, visited)
            visited.pop()

            return satisfies

        length  = len(board) 
        breadth = len(board[0]) if len(board) else 0

        satisfies = False
        # for i in board:
            # print(i)
        for i in range(0, length):
            for j in range(0, breadth):
                # print(i,j)
                if explore(i, j, '', [(-1, -1)]):
                    
                    return True
        return False