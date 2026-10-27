class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        pred = lambda x: x==len(nums) or nums[x] <= nums[len(nums)-1]

        while lo<hi:
            mid = lo + (hi-lo)//2
            if pred(mid):
                hi = mid
            else:
                lo = mid+1
        return nums[lo]
        