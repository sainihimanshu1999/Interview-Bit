class Solution:
    def distance(self,A,B):
        A = list(A)
        B = list(B)
        m = len(A)
        n = len(B)
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(m):
            for j in range(n):
                #swap
                a = dp[i][j]+(0 if A[i]==B[j] else 1)
                #remove
                b = dp[i][j+1]+1
                #add
                c = dp[i+1][j]+1

                dp[i+1][j+1] = min(a,b,c)

        return dp[m][n]