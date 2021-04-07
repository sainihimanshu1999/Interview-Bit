class Solution:
    def solve(self,A,B):
        n = len(A)
        m = len(B)

        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(1,n+1):
            dp[0][i] = 1

        for i in range(1,m+1):
            for j in range(i,n+1):
                if i == 1 and j==1:
                    if B[i-1]==A[j-1]:
                        dp[i][j] = 1
                else:
                    if B[i-1]==A[j-1]:
                        dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                    else:
                        dp[i][j] = dp[i][j-1]

        return dp[m][n]