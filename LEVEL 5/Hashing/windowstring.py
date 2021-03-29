class Solution:
    def minWindow(self, A, B):
        T = {}
        num_uniq = 0
        for c in B:
            if c in T:
                x = T[c]
                T[c] = x-1
            else:
                T[c] = 0
                num_uniq += 1
        
        count_uniq = 0
        head = 0
        tail = 0
        ans = ''

        while(True):
            if count_uniq<num_uniq:
                if head == len(A):
                    break
                c = A[head]
                if c in T:
                    x = T[c]
                    if x == 0:
                        count_uniq += 1
                    T[c] = x+1
                head += 1
            else:
                if ans == '':
                    ans = A[tail:head]
                else:
                    if len(ans) > (head-tail):
                        ans = A[tail:head]
                c = A[tail]
                if c in T:
                    x = T[c]
                    if x ==  1:
                        count_uniq -=1
                    T[c] = x-1
                tail += 1
        return ans
            


