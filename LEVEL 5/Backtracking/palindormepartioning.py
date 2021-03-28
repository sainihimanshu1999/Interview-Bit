def partition(self, A):
        n=len(A)
        res=[]

        def dfs(op,k):
            if k==n:
                res.append(op)
                return
            for i in range(k,n):
                temp=A[k:i+1]
                if temp==temp[::-1]:
                    dfs(op+[temp],i+1)
            
        dfs([],0)
        return res