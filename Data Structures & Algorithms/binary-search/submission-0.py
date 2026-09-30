class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e = 0, len(nums)-1
        

        while s<=e:
            mid = int((s+e)/2)
            print(mid)
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                e = mid-1
            elif target>nums[mid]:
                s = mid+1
        
        return -1
        