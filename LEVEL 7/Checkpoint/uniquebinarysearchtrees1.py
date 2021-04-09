class Solution:
    def genTrees(self,A):
        if A ==0 :
            return []
        def xTrees(start,end):
            trees = []
            for i in range(start,end):
                for left in xTrees(start,i):
                    for right in xTrees(i+1,end):
                        trees.append(TreeNode(i))
                        trees[-1].left = left
                        trees[-1].right = right
            return trees if trees else [None]

        return xTrees(1,A+1)