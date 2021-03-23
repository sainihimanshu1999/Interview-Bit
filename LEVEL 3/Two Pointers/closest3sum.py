class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        i = 0
        ans = A[0] + A[1] + A[2]
        A.sort()
        for i in range(len(A)-2):
            l = i+1
            r = len(A)-1
            while l<r:
                if abs(ans-B) > abs(A[i]+A[l]+A[r] - B):
                    ans = A[i]+A[l]+A[r]
                    
                if A[i]+A[l]+A[r]>B:
                    r -= 1
                elif A[i]+A[l]+A[r]<B:
                    l+=1
                else:
                    return B
        return ans
                
