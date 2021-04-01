def order(self,A,B):
    l = dict()
    for i in range(len(A)):
        l[A[i]] = B[i]
    x = []
    for i in A:
        x.insert(l[i],i)
    return x


'''
Time complexity is O(n^2)
'''

