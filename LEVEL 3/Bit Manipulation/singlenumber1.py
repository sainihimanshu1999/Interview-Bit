class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        A=sorted(A)
        i=0
        j=1
        while (j<len(A)):
            if A[i]==A[j]:
                i=j+1
                j=j+2
                
            else:
                return A[i]
                
        else:
            return A[i]
