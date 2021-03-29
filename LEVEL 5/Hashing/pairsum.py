class Solution:
    def equal(self,A):
        pairsum = {}
        equals = []

        for i in range(len(A)):
            for j in range(i+1,len(A)):
                s = A[i]+A[j]
                if s in pairsum:
                    if i not in parisum[s][-1] and j not in pairsum[s][-1]:
                        pairsum[s].append([i,j])
                    else:
                        pairsum[s] = [[i,j]]

                    if len(pairsum[s]) ==  2:
                        equals.append(pairsum[s][0] + pairsum[s][1])
            equals.sort()
            return equals[0]