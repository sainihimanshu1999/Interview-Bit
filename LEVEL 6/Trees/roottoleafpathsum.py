class Solution:
    def sumNumber(self,A):

        def solve(root,value):
            if not root:
                return 0
            value = (value*10+root.val)
            #leaf node
            if not root.left and not root.right:
                return value
            return(solve(root.left,value)+solve(root.right,value))
        return (solve(A,0))%1003