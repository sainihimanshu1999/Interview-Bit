class Solution:
    def LCS(self,A,B):
        m = len(A)
        n = len(B)

        L = [[None]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j==0:
                    L[i][j] = 0
                elif A[i-1]==B[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[m][n]






'''
Longest common sequence, if found equal then diagonal+1 and if not then max(top,left) in DP table
'''


