class Solution:
    def colorful(self,A):
        A = list(str(A))
        products = set()
        for i in range(len(A)):
            p = 1
            for j in range(i,len(A)):
                p *=int(A[j])

                if p not in products:
                    products.add(p)
                else:
                    return 0
        return 1