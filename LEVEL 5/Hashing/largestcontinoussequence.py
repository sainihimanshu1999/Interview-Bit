class Solution:
    def lszeros(self,A):
        mp = {0:-1}
        start = end = 0
        s = 0
        for i in range(len(A)):
            s += A[i]

            if s in mp:
                if i-mp[s]>end-start:
                    start = mp[s]
                    end = i
            else:
                mp[s] = i
        return A[start+1:end+1]