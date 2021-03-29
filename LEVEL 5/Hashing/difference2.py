class Solution:
    def defPossible(self, A, B):
        A = list(A)
        A.sort()
        ans = {}
        for i in range(len(A)):
            if A[i] in ans:
                return 1
            else:
                ans[B+A[i]] = i
        return 0