class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        arr = []
        for i in range(A):
            arr.append(i+1)
        x =[[]]
        for i in range(len(arr)):
            for j in range(len(x)):
                x.append(x[j]+[arr[i]])
                
        c = []
        for q in x:
            if len(q)==B:
                c.append(q)
        c.sort()
        return c
        
