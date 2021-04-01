class Solution:
    def pathSum(self,A):
        if not A:
            return 0
        if not A.left and not A.right:
            return 1 if A.val == B else 0
        
        return self.pathSum(A.left, B-A.val) or self.pathSum(A.right, B-A.val)
        