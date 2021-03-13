class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        currRow = []
        currRow.append(1)
        
        if A == 0:
            return currRow
        
        prev = self.getRow(A-1)
        
        for i in range(1,len(prev)):
            curr = prev[i-1]+ prev[i]
            currRow.append(curr)
            
        currRow.append(1)
        
        return currRow
