'''
building tree from given inorder traversal
'''

class Solution:
    def buildTree(self,A):
        if not A:
            return None
        maxval = max(A)
        maxindex = A.index(maxval)

        root = TreeNode(maxval)
        root.left = self.buildTree(A[:maxindex])
        root.right = self.buildTree(A[maxindex+1:])
        return root