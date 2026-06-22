class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def backtrack(index, curr):
            if index == len(nums):
                result.append(curr[:])
                return
                
            backtrack(index+1, curr)
            curr.append(nums[index])
            backtrack(index+1, curr)
            curr.pop()
            
        backtrack(0, [])
        return result
        