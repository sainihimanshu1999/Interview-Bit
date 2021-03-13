import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def checkPrime(self,n):

        if n==1:
            return False
        
        for i in range(2,int(math.sqrt(n))+1):
    
            if n%i==0:
                return False
        return True
            
    def primesum(self, A):
        for i in range(1,A//2+1):
            if self.checkPrime(i) and self.checkPrime(A-i):
                return i,A-i
            
        
'''
first we are checking prime numbers and then we can using limit like A//2+1 and then checking prime 
number again and then returning
'''