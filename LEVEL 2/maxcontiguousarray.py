def maxSubArray(self, A):
        n = len(A)
        max_so_far = A[0]
        curr_max = A[0]
        
        for i in range(1,n):
            curr_max = max(A[i],curr_max + A[i])
            max_so_far = max(max_so_far,curr_max)
        return max_so_far