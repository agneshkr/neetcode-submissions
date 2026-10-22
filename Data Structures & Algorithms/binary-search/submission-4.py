class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo, hi = 0, len(nums)
        pred = lambda x: target <= nums[x]
        while lo<hi:
            mid= lo +(hi-lo)//2

            if pred(mid):
                hi = mid
            else:
                lo = mid+1
        if lo!=hi:
            raise
        return lo if (lo < len(nums) and nums[lo]==target) else -1
            # if nums[mid]==target:
            #     return mid

            # elif nums[mid] > target:
            #     hi = mid-1
            # else:
            #     lo = mid+1
            
        