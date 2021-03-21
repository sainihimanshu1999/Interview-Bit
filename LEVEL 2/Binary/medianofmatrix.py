class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        n = len(A)
        m = len(A[0])
        
        x = []
        for i in range(n):
            for j in range(m):
                x.append(A[i][j])
                
        x.sort()
        k = m*n
        k = (k+1)//2
        return x[k-1]