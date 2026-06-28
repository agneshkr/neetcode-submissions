class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        nums = sorted(candidates)
        def explore(idx, curr, total):

            if total == target:
                results.append(curr[:])
                return
            elif (total > target) or (idx >= len(nums)):
                return

            curr.append(nums[idx])
            explore(idx+1, curr, total+nums[idx])
            curr.pop()
            nxt = idx+1
            while nxt and nxt<len(nums):
                if nums[nxt] == nums[nxt-1]:
                    nxt=nxt+1
                else:
                    break
            explore(nxt, curr, total)
            

            


        explore(0, [], 0)
        return results