A=sorted(A)
Max=0
for i in range(len(A)-1):

        diff=0
        diff=A[i+1]-A[i]
        if diff>Max:
            Max=diff
return Max