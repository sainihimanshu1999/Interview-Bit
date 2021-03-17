from itertools import groupby
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        t = '1'
        for i in range(1,A):
            a = [''.join(group) for key, group in groupby(t)]
            t = ''
            for i in a:
                t = t+str(len(i))+i[0]
        return t
