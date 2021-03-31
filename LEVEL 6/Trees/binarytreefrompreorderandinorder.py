class Solution:
    def buildTree(self,A,B):
        if not B:
            return None
        root_pos = B.index[A[0]]
        root = TreeNode(A[0])
        root.left = self.buildTree(A[1:root_pos+1],B[:root_pos])
        root.right = self.buildTree(A[root_pos+1:],B[root_pos+1:])
        return root
