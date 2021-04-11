class Solution:
   def generateMatrix(self, A):
        left = False
        right = True
        down = False
        up = False
        
        op = [[0]*A for i in range(A)]
        
        val = 1
        row = 0
        col = 0
        
        while val <= A**2:
            if right and col<A:
                op[row][col] = val
                
                val+=1
                col+=1
                if col==A or op[row][col]!=0:
                    right = False
                    down = True
                    col -= 1
                    row += 1
                    continue
            if down and row<A:
                op[row][col] = val
                
                val += 1
                row += 1
                
                if row == A or op[row][col]!=0:
                    down = False
                    left = True
                    row -= 1
                    col -= 1
                    continue
                    
            if left and col>=0:
                op[row][col] = val
                val += 1
                col -=1
                
                if col == -1 or op[row][col]!=0:
                    left = False
                    up = True
                    row -= 1
                    col += 1
                    continue
            if up and row>=0:
                op[row][col] = val
                val += 1
                row -= 1
                if row == -1 or op[row][col]!=0:
                    up = False
                    right = True
                    col += 1
                    row +=1
                    continue
        
        return op
                
                
                
                
                
                
                