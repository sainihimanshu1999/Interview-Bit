class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        if B<A[0]:
            return 0
        l = 0
        h = len(A)-1
        nearest_min = float('-inf')
        index = 0
        while l<=h:
            m = l+(h-l)/2
            if A[m]==B:
                return m
            if A[m] < B and float(A[m]) > nearest_min:
                nearest_min = float(A[m])
                index = m
            if B < A[m]:
                h = m-1
            else:
                l = m+1
        
        
        return index+1
            