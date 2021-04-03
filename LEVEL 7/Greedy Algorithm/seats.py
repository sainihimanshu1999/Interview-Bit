class Solution:
    def seats(sefl,A):
        if 'x' not in A:
            return 0
        if len(A)== 1:
            return 0

        x_Array = [i for i in range(0,len(A)) if A[i] == 'x']
        if sorted(x_Array) == range(min(x_Array),(x_Array)+1):
            return 0
        else:
            count = 0
            mid = len(x_Array)//2
            for i in range(0,len(A)):
                count += abs(x_Array[i]-x_Array[mid]) - abs(i-mid)
            return count%10000003

        