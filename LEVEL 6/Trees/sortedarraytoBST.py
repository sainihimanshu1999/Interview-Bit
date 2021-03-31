class Solution:
    def sortedArrayToBST(self,A):
        if len(A)==0:
            return None
        mid = len(A)//2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid+1:])
        return root