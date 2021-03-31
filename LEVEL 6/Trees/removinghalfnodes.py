'''
Half nodes are which have only one child
leaf nodes doesn't count as half nodes as their both nodes are NULL
'''
class Solution:
    def solve(self,A):
        if not A:
            return None
        else:
            if(A.left and not A.right):
                return self.solve(A.left)
            elif(A.right and not A.left):
                return self.solve(A.right)
            A.left = self.solve(A.left)
            A.right = self.solve(A.right)
            return A

