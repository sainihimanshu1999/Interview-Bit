class Solution:
    def minDepth(self,A):
        if not A:
            return 0
        
        if not A.left and not A.right:
            return 1
        
        if not A.left:
            return self.minDepth(A.right)+1
        
        if not A.right:
            return self.minDepth(A.left)+1

        return 1+ min(self.minDepth(A.left),self.minDepth(A.right))