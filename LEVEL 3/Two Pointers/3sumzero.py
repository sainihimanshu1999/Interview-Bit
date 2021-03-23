class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        b = []
        c = []
        for i in range(0,len(A)-1):
            l = i+1
            r = len(A)-1
            x = A[i]
            
            while(l<r):
                if(x+A[l]+A[r]==0):
                    b.append([x,A[l],A[r]])
                    
                    l+= 1
                    r-=1
                elif(x+A[l]+A[r]<0):
                    l+=1
                else:
                    r-=1
        b.sort()
        n = len(b)
  
    # to remove duplicates
        for i in range(n): 
            if(i < n-1 and b[i] == b[i+1]): 
                while (i < n-1 and (b[i] == b[i+1])): 
                    i+=1; 
                  
            else: 
                c.append(b[i])
        return c
                
                
