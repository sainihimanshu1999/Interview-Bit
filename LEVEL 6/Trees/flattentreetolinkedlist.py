# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, A):
        curr = A
        stack = []
        while curr or stack:
            while curr:
                if curr.right:
                    stack.append(curr.right)
                curr.right =curr.left
                curr.left = None
                prev =curr
                curr = curr.right
                
            if stack:
                prev.right = stack.pop()
                curr = prev.right
        return A
                
                
                    
                