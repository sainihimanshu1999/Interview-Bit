class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        n = len(A)
        ans = 0 
        for i in range(0, 32): 
            count = 0
            for j in range(0, n): 
                if ( (A[j] & (1 << i)) ): 
                    count+= 1
      
            ans += (count * (n - count) * 2); 
          
        return ans 
