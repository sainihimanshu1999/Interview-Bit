class Solution:
    def flip(self, A):
        l = []
        left = -1
        right = -1
        maxCount = 0
        count = 0
        currleft = 0
        reset = True
        
        for i in range(len(A)):
            if A[i] == '0':
                if reset:
                    currleft = i
                    reset = False
                count += 1
                
            else:
                if count>maxCount:
                    maxCount = count
                    left = currleft +1
                    right = i
                    
                if count>0:
                    count -=1
                    
                else:
                    count = 0
                    reset = True
                    
        if count>maxCount:
            maxCount = count
            left = currleft+1
            right = len(A)
            
        if right>(-1):
            l.append(left)
            l.append(right)
        
        return l
        
                
