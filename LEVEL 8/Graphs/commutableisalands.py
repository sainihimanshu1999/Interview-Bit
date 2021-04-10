class Solution:
    def paths(self,A,B):
        par = [-1]*(A+1)

        def partens(x):
            if par[x] == -1:
                return x
            par[x] = partens(par[x])
            return par[x]

        B.sort(key = lambda x:x[2])
        cost  =0
        while B:
            x,y,c = B.pop(0)
            px = partens(x)
            py = partens(y)
            if px!=py:
                cost+=c
                par[px] = py
        return cost