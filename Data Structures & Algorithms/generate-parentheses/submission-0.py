class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        results = []
        
        left = ['(']*n
        right = [')']*n

        def explore(left, right, curr):

            if (not left) and (not right):
                results.append(curr)
                return
            
            if (len(left)-len(right)) < 0:
                # we have an option to choose left or right 

                # push left
                if left:
                    explore(left[1:], right, curr+left[0])
                # push right
                explore(left, right[1:], curr+right[0])

            else:
                if left:
                    curr=curr+left[0]
                    explore(left[1:], right, curr)




        explore(left, right, '')
        return results
        