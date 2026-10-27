class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo, hi = 0, n
        pred =lambda x: x==n or nums[x] <= nums[len(nums)-1]
        
        while lo<hi:
            mid = lo + (hi-lo)//2
            if pred(mid):
                hi=mid
            else:
                lo=mid+1
        
        # lo is where the rotation happened check if the value is to the right or left of this.
        if target > nums[n-1]:
            lo, hi = 0, lo
        else:
            lo, hi = lo, n 

        pred = lambda x: nums[x]>=target
        while lo<hi:
            mid = lo + (hi-lo)//2
            if pred(mid):
                hi=mid
            else:
                lo=mid+1
        return lo if (0<=lo<n and nums[lo]==target) else -1
