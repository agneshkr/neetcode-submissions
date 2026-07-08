class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        visited = [False]*len(nums)
        def explore(curr, visited):
            
            if len(curr) == len(nums):
                results.append(curr[:])
                return

            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                curr.append(nums[i])
                visited[i] = True  
                explore(curr, visited)
                curr.pop()
                visited[i] = False



        explore([], visited)
        return results