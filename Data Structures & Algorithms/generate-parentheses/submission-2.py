class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        results = []

        def explore(open_remaining, close_remaining, curr):


            if (open_remaining==0) and (close_remaining==0):
                results.append(curr)
                return 

            if open_remaining < close_remaining:
                # we have options to select either one

                # select open again
                if open_remaining:
                    explore(open_remaining-1, close_remaining, curr+'(')
                # select close. valid since open_remaining is less than close_remaining
                explore(open_remaining, close_remaining-1, curr+')')

            else:
                explore(open_remaining-1, close_remaining, curr+'(')


        explore(n, n, '')
        return results