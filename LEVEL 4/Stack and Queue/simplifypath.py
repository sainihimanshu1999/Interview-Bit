class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        s = A.split('/')
        res = '/'
        stack = []
        
        for i in range(len(s)):
            if s[i] != '' and s[i].isalpha() == True:
                stack.append(s[i])
            elif s[i] != '' and len(stack) !=0 and s[i]=='..':
                stack.pop()
                
        if len(stack)!=0:
            for i in range(len(stack)):
                res += stack[i]+'/'
        else:
            res = '/'
            
        if len(res)>1:
            res = res.rstrip('/')
            return res
        return res
        
