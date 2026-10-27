class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles) # rate of bananas 

        def pred(x):
            time_taken = 0
            for pile in piles:
                time_taken+=(pile+x-1)//x
            return time_taken <= h

        while lo<hi:
            mid = lo + (hi-lo)//2
            if pred(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
        