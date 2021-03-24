from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
	    x = deque()
	    numbers = []
	    
        for i in range(len(A)):
            while x and A[i]>=A[x[-1]]:
                x.pop()
            x.append(i)
            
            if i>=B and x and x[0]==i-B:
                x.popleft()
            if i>=B-1:
                numbers.append(A[x[0]])
        return numbers
	            
	    
	    
