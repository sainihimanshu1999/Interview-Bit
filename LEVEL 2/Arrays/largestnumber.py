def largestNumber(self, A):
    maxsize = minsize = 1
    for x in A:
        maxsize = max(maxsize,len(str(x)))
        minsize = min(minsize,len(str(x)))
    return str(int(''.join(sorted(map(str, A), key=lambda s: s*(maxsize//minsize))[::-1])))