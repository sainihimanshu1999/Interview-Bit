class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = A[::-1]
        m = len(A)
        
        DP = [[None]*(m+1) for i in range(m+1)]
  
        for i in range(m+1):
            for j in range(m+1):
                if i == 0 or j == 0 :
                    DP[i][j] = 0
                elif A[i-1] == B[j-1]:
                    DP[i][j] = DP[i-1][j-1]+1
                else:
                    DP[i][j] = max(DP[i-1][j] , DP[i][j-1])
                    
        return DP[m][m]
