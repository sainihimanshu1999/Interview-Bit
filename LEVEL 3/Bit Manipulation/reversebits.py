class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        x = '{:032b}'.format(A)
        return int(x[::-1],2)