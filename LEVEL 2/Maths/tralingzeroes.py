class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        while(A>=5):
            A //= 5
            count += A
        return count