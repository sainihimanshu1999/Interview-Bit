class Solution:
    def linkedlistoBST(self,A):

        arr = []
        temp  =  A
        while temp:
            arr.append(temp.val)
            temp = temp.next

        def BST(x):
            if len(x)==0:
                return None
            
            mid = len(x)//2
            root = TreeNode(x[mid])
            root.left = BST(x[:mid])
            root.right = BST(x[mid+1:])
            return root
        return BST(arr)