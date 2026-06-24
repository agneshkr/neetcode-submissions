class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results=[]
    
        def explore(curr):

            
            for i in nums:

                if len(curr) == len(nums):
                    results.append(curr[:])
                    return

                if i in curr:
                    continue
                curr.append(i)
                explore(curr)
                curr.pop()
        explore([])

        return results