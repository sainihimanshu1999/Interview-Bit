class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, n):
        arraySize = n * 2 - 1; 
        result = [[0 for x in range(arraySize)]  
                     for y in range(arraySize)]; 
              
        # Fill the values 
        for i in range(arraySize): 
            for j in range(arraySize): 
                if(abs(i - (arraySize // 2)) >  
                   abs(j - (arraySize // 2))): 
                    result[i][j] = abs(i - (arraySize // 2)) + 1; 
                else: 
                    result[i][j] = abs(j - (arraySize // 2)) + 1;
                    
        return result
                  
