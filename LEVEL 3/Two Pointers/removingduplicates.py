class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        p1  = 0
        p2 = 1
        for i in range(1,len(A)):
            if A[i]!=A[p1]:
                p1 = p2
                A[i],A[p2] = A[p2],A[i]
                p2+=1
        return p2
                
                
