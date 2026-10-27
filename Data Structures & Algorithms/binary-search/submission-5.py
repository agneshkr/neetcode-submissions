class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        pred = lambda x: nums[x]>=target
        while lo < hi:
            mid = lo + (hi-lo)//2

            if pred(mid):
                hi=mid
            else:
                lo=mid+1
        return lo if (lo<len(nums) and nums[lo]==target) else -1
        