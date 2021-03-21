class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A=int(A)
        if A==1:
            return 0
        x=bin(A)
        if x.count('1')>1:
            return 0
        else:
            return 1