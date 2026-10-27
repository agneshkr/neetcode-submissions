class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        total = rows*cols

        lo, hi = 0, total
        pred = lambda x: matrix[x//cols][x%cols] >= target # this is of form F F F ... T T T
        while lo<hi:

            mid = lo + (hi-lo)//2
            if pred(mid):
                hi=mid
            else:
                lo=mid+1
        return True if (lo<total and matrix[lo//cols][lo%cols]==target) else False

        