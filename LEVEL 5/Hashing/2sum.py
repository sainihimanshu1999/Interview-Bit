class Solution:
    def twoSum(self,A,B):   
        list = {}
        for i,v enumerate(A):
            if B-v in list:
                return list[B-v]+1,i+1
            elif v not in list:
                list[v] = i
        return []