class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
	    n = len(A)
	    res = 0
	    for i in range(1,n):
	        a = abs(A[i]-A[i-1])
	        b = abs(B[i]-B[i-1])
	        m = max(a,b)
	        res += m
        return res
	        