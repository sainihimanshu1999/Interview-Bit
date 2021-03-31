'''
Inverting the tree means left node becomes right node and vice versa, in every subtree of a tree
'''

class Solution:
    def invertTree(self,A):
        A.left,A.right = A.right,A.left
        self.invertTree(A.left)
        self.invertTree(A.right)
        return A