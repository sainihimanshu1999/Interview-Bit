'''
This is a time optimal solution
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        counts = {}
        for i in A:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
            if((counts[i])>(len(A)/3)):
                return i
        return -1
                


'''
This is not a time optimal solution
'''
def repeatedNumber(self, A):
        for i in A:
            if((A.count(i))>(len(A)/3)):
                return i
        return -1