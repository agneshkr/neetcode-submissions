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
                if i in visited:
                    continue
                curr.append(i)
                visited[i] = True
                explore(curr)
                del visited[i]
                curr.pop()

        explore([])
        return results