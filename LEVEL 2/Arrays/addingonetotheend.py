def removezero(a):
        n = len(a)
        ind = -1
        for i in range(n):
            if a[i]!=0:
                ind = i
                break
        if ind==-1:
            return None
        
        b= [0]*(n-ind)
        for i in range(n-ind):
            b[i] = a[ind+i]
        
        return b


class Solution:
    # @param A : list of integers
    # @return a list of integer
        
    
    
    
    def plusOne(self, a):
        n = len(a)
        
        a[n-1] += 1
        carry = a[n-1]/10
        a[n-1] = a[n-1]%10
        
        for i in range(n-2,-1,-1):
            if(carry == 1):
                a[i]+= 1
                carry = a[i]/10
                a[i] = a[i]%10
        
        if(carry==1):
            a.insert(0,1)
  
        p = removezero(a) 
        return p
