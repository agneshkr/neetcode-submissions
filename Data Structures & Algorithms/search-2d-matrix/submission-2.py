class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        total = r*c
        lo, hi = 0, total
        pred = lambda x: target <= matrix[x//c][x%c]

        while lo<hi:
            mid = lo + (hi-lo)//2
            if pred(mid):
                hi = mid
            else:
                lo = mid+1
        return True if (lo<total and matrix[lo//c][lo%c]==target) else False 
        