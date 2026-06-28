class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        results = []

        def explore(curr):
            
            if len(curr) == len(nums):
                results.append(curr[:])
                return 

            for idx, i in enumerate(nums):

                if idx in visited:
                    continue

                curr.append(i)
                visited.add(idx)
                explore(curr)
                curr.pop()
                visited.remove(idx)


        explore([])
        return results