class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        c = []
        p1 = 0
        p2 = 0
        
        while p1<len(A) and p2<len(B):
            if A[p1] == B[p2]:
                c.append(A[p1])
                p1 += 1
                p2 += 1
            elif A[p1]>B[p2]:
                p2+=1
            else:
                p1+=1
        return c
            
            
                
'''
self confidence and always check the corner cases and be careful if the arrays are sorted.
try to solve the problems by decoding the question and carefully analysing it.
'''