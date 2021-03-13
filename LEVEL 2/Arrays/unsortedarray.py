class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        e = n-1
        
        for s in range(n-1):
            if A[s]>A[s+1]:
                break
        if s== n-1:
            return -1
            exit()
            
        while e>0:
            if A[e]<A[e-1]:
                break
            e -=1
            
        max = A[s]
        min = A[s]
        
        for i in range(s+1,e+1):
            if A[i]>max:
                max = A[i]
            if A[i]<min:
                min = A[i]
                
        for i in range(s):
            if A[i]>min:
                s = i
                break
        i = n-1
        while i >e+1:
            if A[i]<max:
                e = i
                break
            i -=1
            
        return A
                
            
