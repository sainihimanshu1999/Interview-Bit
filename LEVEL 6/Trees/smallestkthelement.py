class Solution:
    def kthelement(self,A,B):
        l = []
        def inordertraversal(root):
            if len(l) == B:
                return
            if root:
                inordertraversal(root.left)
                l.append(root.val)
                inordertraversal(root.right)
            inordertraversal(A)
            return l[B-1]


'''
Used inorder traversal because it provides sorted array
'''