class Solution:
    def buildTree(self,A,B):
        if not A:
            return None
        root_pos =  A.index(B[-1])
        root = TreeNode(B[-1])
        root.left = self.buildTree(A[:root_pos],B[:root_pos])
        root.right = self.buildTree(A[root_pos+1:],B[root_pos:-1])
        return root