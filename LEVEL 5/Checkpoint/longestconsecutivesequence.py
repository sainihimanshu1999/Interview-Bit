class Solution:
    def lenghtoflongestconsecutiveseq(self,A):
        s = set()
        res = 0
        n = len(A)
        for i in A:
            s.add(i)

        for i in range(n):
            if (A[i]-1) not in s:
                j = A[i]
                while(j in s):
                    j += 1
                res = max(ans,j-A[i])
        return res