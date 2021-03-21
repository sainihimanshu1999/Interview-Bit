class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        A = int(A,2)
        B = int(B,2)
        A = A+B
        a = bin(A).replace('0b','')
        return a
        