class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        for i in A:
            if i == B:
                return A.index(i)
        return -1
