class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        A.sort()
        c = ''
        if len(A[0]) > len(A[-1]):
            a = A[0]
            b = A[-1]
        else:
            b = A[0]
            a = A[-1]
            
        for i in range(len(b)):
            if a[i] == b[i]:
                c += a[i]
                
        return c