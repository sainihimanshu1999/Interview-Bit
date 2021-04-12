class Solution:
    def solve(self,A):
        n = len(A)
        ans = 0

        for i in range(1,(n-1)):
            max1 = 0
            max2 = 0

            for j in range(0,i):
                if A[j]<A[i]:
                    max1 = max(max1,A[j])

            for j in range(i+1,n):
                if A[j]>A[i]:
                    max2 = max(max2, A[j])
            
            if max1 and max2:
                ans = max(ans, max1 + A[i]+ max2)
        
        return ans