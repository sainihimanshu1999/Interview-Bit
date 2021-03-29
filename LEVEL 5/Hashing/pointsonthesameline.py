class Solution:
    def maxPoints(self,A,B):
        if len(A)<2:
            return len(A)
        maxi = 0
        for i in range(len(A)-1):
            mp = {}
            repeated_pts = 0
            for j in range(i+1,len(A)):
                if A[i]!=A[j]:
                    x_diff = A[j] - A[i]
                    y_diff = B[j] - B[i]
                    slope = float(y_diff)/float(x_diff)
                elif B[j]==B[i]:
                    repeated_pts += 1
                    continue
                else:
                    slope = 'undefined'
                if mp.get(slope):
                    mp[slope] += 1
                else:
                    mp[slope] = 1
            for key.value in mp.items():
                maxi = max(maxi, value+repeated_pts)
            if len(mp)==0:
                maxi = max(value,repeated_pts)
        return maxi+1

