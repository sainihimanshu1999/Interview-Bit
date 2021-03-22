class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        if abs(B) == 1:
            return A*B
        
        
        sign = -1 if((A<0)^(B<0)) else 1
        
        A = abs(A)
        B = abs(B)
        
        quotient = 0
        while(A >= B):
            A -= B
            quotient += 1
        
        return sign * quotient
