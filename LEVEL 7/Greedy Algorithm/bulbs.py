class Solution:
    def bulbs(self,A):
        flip = 0
        current_State = 0
        for i in range(len(A)):
            if current_State == 0:
                curr_bulb = A[i]
            else:
                curr_bulb = 1  if A[i]==0 else 0

            if curr_bulb == 0:
                flip +=1 
                current_State = 1 if current_State ==0  else 0
        
        return flip