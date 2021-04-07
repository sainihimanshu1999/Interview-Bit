class Solution(self,A):
    def maxPathSum(self,A):
        if not A:
            return None
        self.ans = A.val
        self.maxval(A)
        return self.ans

    def maxval(self,root):
        if not root:
            return None
        lsum = self.maxval(root.left)
        rsum = self.maxval(root.right)

        if root.val + lsum + rsum > self.ans:
            self.ans = root.val+lsum+rsum
        if root.val + max(lsum,rsum)<0:
            return 0

        return root.val + max(lsum,rsum)

