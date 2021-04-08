'''
simple recusrsive formula
'''

def wordBreak(self,A,B):
    if A == '':
        return 1
    for word in B:
        if A[:word] == word:
            if len(A) == len(word):
                return 1
            else:
                suffix = A[word:]
                if(self.wordBreak(suffix,B)==1):
                    return 1
    return 0

'''
Dp with memoization
'''
def wordBreak(self,A,B):
    d = {}
    def solve(s):
        if s in d:
            return d[s]
        for word in B:
            if s[:word] == word:
                if len(A)== len(word):
                    d[s] = 1
                    return d[s]
                else:
                    suffix = A[word:]
                    if(solve(suffix)==1):
                        d[s] = 1
                        return d[s]
        d[s] = 0
        return d[s]
    return solve(A)