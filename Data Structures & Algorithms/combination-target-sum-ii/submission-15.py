class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        results = []
        candidates = sorted(candidates)
        print(candidates)
        def explore(idx, curr, total):

            if total == target:
                results.append(curr[:])
                return
            elif idx == len(candidates) or total > target:
                return
            curr.append(candidates[idx])
            explore(idx+1, curr, total+candidates[idx])
            curr.pop()
            nxt = idx+1
            while nxt < len(candidates) and candidates[nxt] == candidates[idx]:
                nxt=nxt+1
            explore(nxt, curr, total)



        explore(0, [], 0)
        return results