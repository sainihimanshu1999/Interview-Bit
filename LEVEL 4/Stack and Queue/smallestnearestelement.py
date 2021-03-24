class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        ans = []
        stack = []
        
        for i in range(len(A)):
            if not len(stack):
                ans.append(-1)
                stack.append(A[i])
            else:
                if stack[-1]<A[i]:
                    ans.append(stack[-1])
                    stack.append(A[i])
                else:
                    stack.pop()
                    
                    while len(stack):
                        if stack[-1]<A[i]:
                            ans.append(stack[-1])
                            stack.append(A[i])
                            break
                        else:
                            stack.pop()
                    else:
                        ans.append(-1)
                        stack.append(A[i])
        return ans
                        
                    
