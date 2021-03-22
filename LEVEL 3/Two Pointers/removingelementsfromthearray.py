class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n = len(A)

        if n==1 and A[0]==B: # handlign edge cases
            return 0
        tracker = 0
        i=0
        
        while i<n: #moving all B's to end using 2 pointer approach
            if A[i]!=B:
                A[i],A[tracker] = A[tracker],A[i]
                tracker+=1
            else:
                A[i],A[tracker] = A[tracker],A[i]
            i+=1
        for i in range(n-1,-1,-1): #counting in reverse
            if A[i]!=B:
                break
        return (i+1)
