class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e = 0, len(nums)-1

        while s<=e:
            mid = s + (e-s)//2

            if nums[mid]==target:
                return mid


            # find where the mid is upper or lower half
            upper_half = nums[mid] >= nums[s]

            if upper_half:
                if target > nums[mid]:
                    s=mid+1
                elif target < nums[mid]:
                    if target>=nums[s]:
                        e=mid-1
                    else:
                        s=mid+1
            else:
                if target < nums[mid]:
                    e=mid-1
                elif target > nums[mid]:
                    if target >=nums[s]:
                        e=mid-1
                    else:
                        s=mid+1 
        
        return -1