def longestsubsequnce(self,A):
    n = len(A)
    dp = [1]*(n+1)

    for i in range(1,n):
        for j in range(0,i):
            if ((A[i]>A[j]) and (dp[i]<dp[j]+1)):
                dp[i] = dp[j] + 1
    return max(dp)