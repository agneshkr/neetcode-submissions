class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False]*len(nums)
        results = []
        nums = sorted(nums)
        def explore(curr):
            
            if len(curr) == len(nums):
                results.append(curr[:])
                return 

            for idx, i in enumerate(nums):

                if visited[idx]:
                    continue
                if idx>0 and nums[idx] == nums[idx-1] and not visited[idx-1]:
                    continue

                curr.append(i)
                visited[idx]=True
                explore(curr)
                curr.pop()
                visited[idx]=False

        explore([])
        return results