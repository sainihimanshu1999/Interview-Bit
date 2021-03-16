class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A == 1:
            return 1
        ans  = [1]*B
        
        for i in range(1,A):
            for j in range(1,B):
                ans[j] += ans[j-1]
        return ans[-1]
        
                