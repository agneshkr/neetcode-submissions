class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        

        ROW, COL = len(matrix), len(matrix[0])


        s, e = 0, ROW*COL-1

        while s<=e:
            mid = s + (e-s) // 2

            row = mid // COL
            col = mid % COL
            v = matrix[row][col]

            if target==v:
                return True
            elif target > v:
                s=mid+1
            else:
                e=mid-1

        return False