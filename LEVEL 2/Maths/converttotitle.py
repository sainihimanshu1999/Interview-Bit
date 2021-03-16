class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        s = ''
        while(A):
            A = A - 1
            s = s+chr((A%26)+ord('A'))
            A = int(A/26)
        return s[::-1]
