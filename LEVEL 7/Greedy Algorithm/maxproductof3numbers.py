class Solution:
    def maxp3(self,A):
        if len(A)<3:
            return 0
        A.sort()
        return(max(A[-1]*A[-2]*A[-3],A[0],A[1],A[-1]))