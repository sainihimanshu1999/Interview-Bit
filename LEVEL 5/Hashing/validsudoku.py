def isValidSudoku(self, A):
    row, col, sec = {}, {}, {}
    for i in range(len(A)):
        row[i], col[i], sec[i] = set(), set(), set()
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != '.':
                s = (i // 3) + 3 * (j // 3)
                if A[i][j] in row[i] or A[i][j] in col[j] or A[i][j] in sec[s]:
                    return 0
                row[i].add(A[i][j])
                col[j].add(A[i][j])
                sec[s].add(A[i][j])
    return 1
