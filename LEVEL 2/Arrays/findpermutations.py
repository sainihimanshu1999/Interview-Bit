class Solution:
    def perm(self,A,B):
        count_D = A.count('D')
        result = []
        result.append(count_D+1)
        low = count_D
        high = count_D+2

        for i in A:
            if i =='I':
                result.append(high)
                high += 1
            else:
                result.append(low)
                low -= 1
        return result