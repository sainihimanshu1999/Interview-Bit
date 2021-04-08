class Solution:
    def longestsub(self,A):
        n =  len(A)
        lis = [1]*(n+1)

        for i in range(1,n):
            for j in range(0,i):
                if ((A[i]>A[j]) and (lis[i]<lis[j]+)):
                    lis[i] = lis[j]+1

        lds = [1]*(n+1)

        for i in reversed(range(n-1)):
            for j in rversed(range(0,n)):
                if ((A[i]>A[j]) and (lis[i]<lis[j]+)):
                    lis[i] = lis[j]+1

        maxi = lis[0]+lds[0]-1

        for i in range(n):
            maxi = max(lis[i]+lds[i]-1,maxi)

        return maxi