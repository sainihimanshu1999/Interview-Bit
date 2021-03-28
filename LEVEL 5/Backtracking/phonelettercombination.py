class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        nums = {0:'0', 1:'1', 2:'abc', 3:'def', 4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        res = [ s for s in nums[int(A[0])]]
        for s in A[1:]:
            t = nums[int(s)]
            new_list = []
            for j in range(len(t)):
                new_list +=[r+t[j] for r in res]
            res = new_list
        res.sort()
        return res
            