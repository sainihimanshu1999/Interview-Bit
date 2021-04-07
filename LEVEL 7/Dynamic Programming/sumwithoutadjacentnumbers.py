class Solution:
    def solve(self,A):
        if len(A[0])==1:
            return max(A[0][0],A[1][0])
        dp = [-10000]*len(A[0])
        dp[0] = max(A[0][0],A[0][1])
        dp[1] = max(A[0][1],A[1][1])

        p = max(dp)
        if len(dp)==2:
            return p
        dp[2] = max(A[0][2],A[1][2]) + dp[0]

        for i in range(3,len(A[0])):
            p = max(dp[i-2],p)
            dp[i] = max(dp[i-1],max(A[0][i],A[1][i])+p)
        return dp[-1]

