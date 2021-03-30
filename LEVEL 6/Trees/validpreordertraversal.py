class Solution:
    def BSTfromPreorder(self,A):
        root = float('-infinity')
        stack = []
        for i in range(len(A)):
            if A[i]<root:
                return 0
            if(stack and stack[-1]<A[i]):
                root = stack.pop()
            stack.append(A[i])
        return 1

'''
In Pre order traversal, if we encounter any number greater than root or current node then every
item we encounter should be greater than root or current node then return 1 else return 0
'''