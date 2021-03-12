class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, arr):
        N=len(arr)
        n=len(arr[0])
        iarr=set()
        jarr=set()
    
        for i in range(N):
            for j in range(n):
                if arr[i][j]==0:
                    if i not in iarr:
                        iarr.add(i)
                    if j not in jarr:
                        jarr.add(j)
                        
        for val in iarr:
            for j in range(n):
                arr[val][j]=0
        for val in jarr:
            for i in range(N):
                arr[i][val]=0
                
        return arr
                
