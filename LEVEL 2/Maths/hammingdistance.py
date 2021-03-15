class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        n = len(A)
        ans = 0  # Initialize result 
  
    # traverse over all bits 
        for i in range(0, 32): 
          
            # count number of elements with i'th bit set 
            count = 0
            for j in range(0, n): 
                if ( (A[j] & (1 << i)) ): 
                    count+= 1
      
            # Add "count * (n - count) * 2" to the answer 
            ans += (count * (n - count) * 2); 
          
        return ans 
                
