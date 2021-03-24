def solve(self, A):
    q= deque()
    cnt_map = {A[0]:1}
    ret = A[0]
    q.append(A[0])
    
    for i in range(1,len(A)):
        ch = A[i]
        if not cnt_map.get(ch):
            cnt_map[ch] = 1
        else:
             cnt_map[ch] += 1
        
        q.append(ch)
        while q and cnt_map[q[0]] != 1:
            q.popleft()
        
        if q:
            ret += q[0]
        else:
            ret += '#'
            
    
    return ret