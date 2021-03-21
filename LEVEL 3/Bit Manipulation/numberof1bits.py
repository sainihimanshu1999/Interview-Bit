class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        x  =bin(A)
        return x.count('1')
