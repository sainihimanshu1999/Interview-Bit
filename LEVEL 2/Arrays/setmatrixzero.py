class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        fcz = False
        for r in range(len(A)):
            if A[r][0] == 0:
                fcz = True
        for r in range(len(A)):
            for c in range(1,len(A[0])):
                if A[0][c] == 0:
                    A[0][c] = 0
                    A[r][0] = 0
        for c in range(1,len(A[0])):
            if A[0][c] == 0:
                for r in range(len(A)):
                    A[r][c] = 0
        for r in range(len(A)):
            if A[r][0] == 0:
                A[r] = [0]*len(A[0])
            if fcz:
                for r in range(len(A)):
                    A[r][0] = 0
            return A
        
