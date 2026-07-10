class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letter_combs = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        idx=2
        mapping={}
        for l in letter_combs:
            mapping[str(idx)] = list(l)
            idx=idx+1
        results = []
        if digits == "":
            return []
        def explore(idx, curr):
            
            if idx == len(digits):
                results.append(curr[:])
                return

            possible_combinations = mapping[digits[idx]]

            for i in possible_combinations:
                explore(idx+1, curr+i)

        explore(0, '')

        return results