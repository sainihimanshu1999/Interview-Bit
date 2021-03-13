class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        total = sum(B)
        if total%3==0:
            target = total//3
        else:
            return 0
        ans = 0
        f = 0
        s = 0
        for i in range(A-1):
            s+=B[i]
            if s==2*target:
                ans += f
            if s== target:
                f += 1
        return ans