class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def explore(idx, curr):
            
            if idx == len(nums):
                results.append(curr[:])
                return

            curr.append(nums[idx])
            explore(idx+1, curr)
            curr.pop()
            explore(idx+1, curr)

        explore(0, [])

        return results
        