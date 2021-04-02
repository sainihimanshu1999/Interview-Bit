# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        def ino(root,l):
            if not root:
                return 
            ino(root.left,l)
            l.append(root.val)
            ino(root.right,l)
        
        l = []
        ino(A,l)
        n = len(l)
        for i in range(1,n):
            if l[i-1]>=l[i]:
                return 0
        return 1
        
        
            
