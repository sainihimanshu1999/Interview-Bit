'''
Post order without recurrsion
'''
def postorder(self,A):
    stack = []
    ans = []
    curr = A
    while stack or curr:
        while curr:
            ans.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            curr = curr.right
            if stack:
                curr = stack.pop()
        return ans