class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        s, e = 1, max(piles)
        best_rate=e
        while s<=e:
            mid = s + (e-s)//2

            hours_spent = 0
            for p in piles:
                hours_spent+=(p+mid-1)//mid
            
            if hours_spent <= h:
                best_rate = mid
                e=mid-1
            else:
                s=mid+1
        
        return best_rate
        