class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        ans = 0
        for i in range(len(A)):
            ans += (ord(A[i])-64)*(26**(len(A)-i-1))
        return ans
