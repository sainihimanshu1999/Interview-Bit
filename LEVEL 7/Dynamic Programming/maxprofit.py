'''
Not using dynamic programming, because it's easy as it is
'''
class Solution:
    def profit(self,A):
        return sum(max(0,A[i]-A[i-1])for i in range(1,len(A)))