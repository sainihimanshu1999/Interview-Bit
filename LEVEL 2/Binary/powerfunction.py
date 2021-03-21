class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        res = 1
        while(n>0):
            if n%2==1:
                res = res*x
                res = res%d
            n = n//2
            x = x*x
            x = x%d
        res = res%d
        return res
