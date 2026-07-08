class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def explore(idx, curr, total):
            
            if total == target:
                results.append(curr[:])
                return
            elif idx == len(nums) or total > target:
                return

            curr.append(nums[idx])
            explore(idx, curr, total+nums[idx])
            curr.pop()
            explore(idx+1, curr, total)

        explore(0, [], 0)
        return results