'''
It is not the most efficient solution, it sometimes give TLE
'''

def numTrees(self,A):
    if A<=1:
        return 1
    ans = 0
    for i in range(A):
        ans += self.numTrees(i)*self.numTrees(A-i-1)
    return res


'''
Time efficieint DP solution
'''

def numTrees(self,A):
    if(A==0 or A==1):
        return 1
    dp = [0]*(A+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,A+2):
        for j in range(i):
            dp[i] = dp[j]*dp[i-j-1]

    return dp[A]