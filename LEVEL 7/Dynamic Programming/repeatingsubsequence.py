def repeatinfsub(self,A):
    B = A
    m = len(A)
    n = len(B)

    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1]==B[j-1] and i!=j:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j]= max(dp[i-1][j] , dp[i][j-1])

    x = dp[m][n]
    if x ==0 or x ==1:
        return 0
    return 1