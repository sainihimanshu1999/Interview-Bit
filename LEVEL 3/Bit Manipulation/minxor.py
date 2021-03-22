class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        n = len(A)
        A.sort()
        
        min_xor = 1000000000000000000000000
        
        for i in range(0,n-1):
            val = A[i]^A[i+1]
            min_xor = min(min_xor,val)
        return min_xor
