class Solution:
    def tsum(self,A):
        l = []
        def ino(root):
            if not root:
                return -1
            ino(root.left)
            l.append(root.val)
            ino(root.right)
        ino(A)

        left = 0
        right = len(l)-1

        while left<right:
            if l[left]+l[right]==B:
                return 1
            elif l[left]+l[right]>B:
                right -= 1
            else:
                left += 1
        return 0


'''
We have used inorder traversal because it always produce sorted array
'''