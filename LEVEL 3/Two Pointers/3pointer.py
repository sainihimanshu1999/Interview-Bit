class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i=j=k=0
        curr = 10**9
        while i < len(A) and j < len(B) and k < len(C):
            curr = min(curr,max(A[i],B[j],C[k]) - min(A[i],B[j],C[k]))
            if min(A[i],B[j],C[k]) is A[i]:
                i+=1
            elif min(A[i],B[j],C[k]) is B[j]:
                j+=1
            else:
                k+=1
        return curr
                    