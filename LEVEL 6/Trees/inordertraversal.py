class Solution:
    def inorder(self,A):
        curr = A
        stack = []
        ans = []
        while(stack!=[]or curr!=None):
            if curr!=None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ans.append(curr.val)
                curr = curr.right
        return ans