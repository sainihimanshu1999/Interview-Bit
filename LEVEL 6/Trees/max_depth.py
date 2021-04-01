def maxDepth(self,A):
    if not A:
        return 0
    return max(self.maxDepth(A.left),self.maxDepth(A.right))+1