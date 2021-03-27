class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        if len(A) == 0:
            return [[]]
        A.sort()
        x = [[]]
        for i in range(len(A)):
            for j in range(len(x)):
                x.append(x[j]+[A[i]])
        x.sort()
        return x