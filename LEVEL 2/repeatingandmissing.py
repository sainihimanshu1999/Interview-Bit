class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        a = []
        numberMap = {}
        max = len(A)
        
        for i in A:
            if i not in numberMap:
                numberMap[i] = True
            else:
                a.append(i)
        
        for i in range(1,max+1):
            if i not in numberMap:
                a.append(i)
        
        return a