class Solution:
    def preorder(self,A):
        res = []
        if not A:
            returr res
        stack = []
        stack.append(A)
        while(stack):
            curr = stack.pop()
            res.append(stack.val)

            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res
