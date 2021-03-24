class Solution:
    # @param A : string
    # @return an integer
    def braces(self,A):
        stack  = []
        ops = ['+','-','*','/']
        
        for i in A:
            if i == '(':
                stack.append(i)
            if i in ops and stack:
                stack.pop()
                
        if not stack:
            return 0
        else:
            return 1
                    
