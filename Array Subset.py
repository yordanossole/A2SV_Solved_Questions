#User function Template for python3
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a_counter = {}
        b_counter = {}
        for A in a:
            if not A in a_counter:
                a_counter[A] = 1
            else:
                a_counter[A] += 1
        
        for B in b:
            if not B in b_counter:
                b_counter[B] = 1
            else:
                b_counter[B] += 1
        
        for B in b:
            if a_counter.get(B,0) < b_counter.get(B,0):
                return False
        
        return True

        # # time will exceed the limit
        # for B in b:
        #     if B in a:
        #         a.remove(B)
        #     else:
        #         return False
        
        # return True
