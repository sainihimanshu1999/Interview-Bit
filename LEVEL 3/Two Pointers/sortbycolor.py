class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        count0 = 0
        count1 = 0
        count2 = 0
        
        n = len(A)
        
        for i in range(n):
            if A[i] == 0:
                count0 += 1
            elif A[i]== 1:
                count1 += 1
            elif A[i] == 2:
                count2 += 1
        
        i = 0
        
        while(count0>0):
            A[i] = 0
            i+=1
            count0 -=1
        
        while(count1>0):
            A[i] = 1
            i+=1
            count1 -= 1
        
        while(count2>0):
            A[i]=2
            i+=1
            count2 -= 1
        return A
