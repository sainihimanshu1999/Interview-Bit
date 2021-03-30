class Solution:
    def kthelement(self,A):
        l = []
        def inordertraversal(root):
            if len(l) == B:
                return
            if root:
                inordertraversal(root.left)
                l.append(root.val)
                inordertraversal(root.right)
            xoxo(A)
            return l[B-1]