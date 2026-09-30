class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e = 0, len(nums)-1
        while s<e:
            mid = s + (e-s)//2
            if nums[mid] > nums[e]:
                s=mid+1
            else:
                e=mid
        return nums[s]