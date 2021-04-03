class Solution:
    def solve(self,A,B):
        A.sort()
        B.sort()
        return max([abs(A[i]-B[i]) for i in range(len(A))])

'''
We had to find the max time taken by a mice to reach to his/her hole
'''