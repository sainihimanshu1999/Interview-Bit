class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        i = 0
        j = 1
        while ( i<=j ) and ( j<n+1 ):
            if (i == j):
                j += 1
            if (A[j]-A[i]==B):
                return 1
            if(A[j]-A[i]<B):
                j += 1
            if(A[j]-A[i]>B):
                i += 1
        return 0
