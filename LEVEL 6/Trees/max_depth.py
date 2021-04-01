def maxDepth(self,A):
    if not A:
        return 0
    return max(self.maxDepth(A.left),self.maxDepth(A.right))+1



'''
Other way of doing it
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A is None:
            return 0
            
        if not A.left  and not A.right:
            return 1
            
        if not A.left:
            return self.maxDepth(A.right)+1
        
        if not A.right:
            return self.maxDepth(A.left)+1
         
        return max(self.maxDepth(A.left), self.maxDepth(A.right))+1
