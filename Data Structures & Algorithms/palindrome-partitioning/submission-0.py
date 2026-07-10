class Solution:
    def partition(self, s: str) -> List[List[str]]:


        results = []

        def explore(idx, curr):
            
            def is_palindrome(dataset):
                for data in dataset:
                    if data != data[::-1]:
                        return False
                return True

            if idx == len(s):
                if is_palindrome(curr):
                    results.append(curr[:])
                    return
                else:
                    return
        
            
            curr.append(s[idx])
            explore(idx+1, curr) # partition
            curr.pop()

            if curr:
                last_entry = curr[-1]
                # only do this if element already exists
                curr[-1] = curr[-1]+s[idx] 
                explore(idx+1, curr) # non partitioned one
                curr[-1] = last_entry


        explore(0, [])

        return results
        