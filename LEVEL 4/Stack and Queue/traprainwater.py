class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        mxleft = [A[0]]
        mxright = [A[n-1]]
        water = []
        
        for i in range(1,n):
            mxleft.append(max(mxleft[i-1],A[i]))
        for i in range(n-2,-1,-1):
            mxright.append(max(mxright[-1],A[i]))
        
        mxright = mxright[::-1]
        
        for i in range(n):
            water.append(min(mxright[i],mxleft[i])-A[i])
        
        return sum(water)
        
