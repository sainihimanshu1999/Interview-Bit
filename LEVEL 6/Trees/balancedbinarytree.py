'''
Way 1 to solcve this question
'''

class Solution:
    # @param A : root node of tree
    # @return an integer
    ans = 1
    def findDepth(self,node,depth):
        if not node:
            return depth -1
        lt_dt = self.findDepth(node.left,depth+1)
        rt_dt = self.findDepth(node.right,depth+1)

        if abs(lt_dt-rt_dt)>1:
            self.ans = 0
        return max(lt_dt,rt_dt)
    def isBalanced(self,A):
        self.findDepth(A,0)
        return self.ans


'''
Way 2 to solve this question
'''

class Solution:
    def height(self,root):
        if not root:
            return None
        return max(self.height(root.right),self.height(root.left))+1
    def isBalanced(self,A):
        if A is None:
            return 1
        lh = self.height(A.left)
        rh = self.height(A.right)
        if abs(lh-rh)<=1 and self.isBalanced(A.right)==1 and self.isBalanced(A.left)==1:
            return 1
        return 0