class Solution:
    def jump(self,A):
        x = 0
        for i,el in enumerate(A):
            if x<i:
                return 0
            x = max(x,i+el)
        return 1