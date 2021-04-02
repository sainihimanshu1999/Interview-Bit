import heapq
class Solution:
    def nmaxpair(self, A, B):
        min_heap = []
        heapq.heapify(min_heap)
        A.sort()
        B.sort()
        n = len(A)
        for i in range(n-1,-1,-1):
            a = A[i]
            pr = min_heap[:]
            for j in range(n-1,-1,-1):
                b = B[j]
                pair_Sum = a+b
                heapq.heappush(min_heap,pair_sum)

                if len(min_heap)>n:
                    x = heapq.heappop(min_heap)

                    if x == pair_Sum:
                        break
            if pr == min_heap:
                break
            return sorted(min_heap)[::-1]