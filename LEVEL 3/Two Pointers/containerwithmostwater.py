class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        l = 0
        r = len(A)-1
        V = 0
        while l < r:
            C = min(A[l], A[r]) * (r - l)
            V = max(V, C)
            if A[l] <= A[r]:
                l += 1
            else: 
                r -= 1
        return V
