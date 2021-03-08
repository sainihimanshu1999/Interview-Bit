def nextPermutation(self, A):
    i = len(A) - 1
    while i>=0 and A[i]<A[i-1]:
        i -= 1
        pivot = A[i - 1]
        j = len(A) - 1
        while j>=i and A[j]<pivot:
            j -= 1
            A[i - 1], A[j] = A[j], A[i - 1]
            ans1 = A[i:]
            ans1.sort()

            ans = A[:i] + ans1
            
    return ans