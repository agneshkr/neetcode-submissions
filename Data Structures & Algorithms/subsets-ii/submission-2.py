class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums = sorted(nums)
        def explore(idx, curr):
            
            if len(nums)==idx:
                results.append(curr[:])
                return
            elif idx>len(nums):
                return
            curr.append(nums[idx])
            explore(idx+1, curr)
            curr.pop()
            nxt=idx+1
            while nxt<len(nums) and nums[nxt]==nums[nxt-1]:
                nxt=nxt+1
            explore(nxt, curr)

        explore(0, [])
        return results        