def solve(self, A):
    from collections import defaultdict
    n = len(A)
    dp = defaultdict(lambda: 1)
    if n == 1: return 1
    for i in range(n):
        for j in range(i):
            k = A[i]-A[j]
            dp[(i, k)] = max(dp[(i, k)], dp[(j, k)]+1)
    return max(dp.values()) if dp.values else 0