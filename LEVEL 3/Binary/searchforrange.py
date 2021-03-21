class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        if B in A:
            t1 = A.index(B)
            A = A[::-1]
            t2 = A.index(B)
            return [t1,len(A)-t2-1]
        return[-1,-1]
