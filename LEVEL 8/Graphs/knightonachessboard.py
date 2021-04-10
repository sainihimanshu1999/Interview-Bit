class Solution:
    def knight(A,B,C,D,E,F):
        visited = [[0]*B for i in range(A)]
        start = (C-1,D-1)
        end = (E-1,F-1)
        if start == end:
            return 0

        def bst(start,end,visited,board):
            count = 0
            queue = []
            queue.append(start[0])
            visited[start[0]][start[1]] = 1

            while queue:
                count += 1
                for x in range(len(queue)):
                    curr = queue[0]
                    queue.pop(0)
                    for val_i,val_j in [(2,-1),(-1,2),(-2,-1),(-1,-2),(-2,1),(1,-2),(2,1),(1,2)]:
                        next_i,next_j = (curr[0]+val_i,curr[1]+val_j)
                        if 0<=next_i<board[0] and 0<=next_j<board[1] and visited[next_i][next_j]==0:
                            if(next_i,next_j)==end:
                                return count
                            visited[next_i][next_j]=1
                            queue.append(next_i,next_j)
            return -1
        return bfs(start,end,visited,(A,B))


'''
It is a very interesting solution, and very clearly explained one, i personally like this solution very much
'''