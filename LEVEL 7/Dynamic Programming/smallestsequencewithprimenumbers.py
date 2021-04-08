def solve(self,A,B,C,D):
    xA,xB,xC = 0,0,0
    nA, nB, nC = A,B,C

    dp = [0]*D
    for i in range(n):
        temp = min(nA,nB,nC)
        dp[i] = temp

        if dp[i] == nA:
            nA = A*dp[xA]
            xA += 1
        
        if dp[i] == nB:
            nB = A*dp[xB]
            xB += 1
        
        if dp[i] == nC:
            nC = A*dp[xC]
            xC += 1
    return dp