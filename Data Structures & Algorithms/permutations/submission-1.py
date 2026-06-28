class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        visited = {}
        def explore(curr):
            
            if len(nums) == len(curr):
                results.append(curr[:])
                return
            elif len(curr) > len(nums):
                return

            for i in nums:
                if i in curr:
                    continue
                curr.append(i)
                explore(curr)
                curr.pop()

        explore([])
        return results