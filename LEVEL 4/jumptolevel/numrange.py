class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def countsub(self,arr, x): 
        
        n = len(arr)
        st = 0
        end = 0
        sum = 0
        cnt = 0
        while end < n : 
            sum += arr[end] 
            
            while (st <= end and sum > x) : 
                sum -= arr[st] 
                st += 1
      
            cnt += (end - st + 1) 
            end += 1
      
        return cnt 
    
    
    def numRange(self, A, B, C):
        RightCount = self.countsub(A,C)
        LeftCount = self.countsub(A,B-1)
        
        return RightCount - LeftCount
        
