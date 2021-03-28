class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
	    if not A:
	        return [[]]
	        
        curr = []
        for i in range(len(A)):
            prev = self.permute(A[:i]+A[i+1:])
            for x in prev:
                curr.append([A[i]]+x)
        return curr
