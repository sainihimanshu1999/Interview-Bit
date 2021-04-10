class Solution:
    def multiple(self,A):
        q = []
        visitedRem = set([])
        q.append('1')

        while q:
            t = q.pop()
            rem = int(t)%A
            if rem == 0:
                return t
            if rem not in visitedRem:
                visitedRem.add(rem)
                q.append(t+'0')
                q.append(t+'1')
                