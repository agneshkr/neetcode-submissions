class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        results = set()

        candidates = sorted(candidates)
        def explore(idx, curr, curr_sum):
            # print(curr)

            if curr_sum == target:
                results.add(tuple(curr))
                # print('got one')
                return 

            if idx >= len(candidates) or curr_sum > target:
                # print('exit')
                return
            
            curr.append(candidates[idx])
            explore(idx+1, curr, curr_sum+candidates[idx])
            curr.pop()
            nxt = idx+1
            while nxt < len(candidates) and candidates[nxt] == candidates[nxt-1]:
                nxt=nxt+1
            explore(nxt, curr, curr_sum)
        explore(0, [], 0)
        return [list(i) for i in results]
        