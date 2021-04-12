class Solution:
    def diagonal(self,A):
        n = len(A)
        N = 2*n - 1
        result = []

        for i in range(N):
            result.append([])

        for i in range(n):
            for j in range(n):
                result[i+j].append(A[i][j])

        return result