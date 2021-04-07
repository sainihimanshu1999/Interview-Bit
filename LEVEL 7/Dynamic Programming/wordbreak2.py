'''
global an local variable
'''

def wordBreak(self,A,B):
    d = {}
    def solve(s):
        if s in d:
            return d[s]
        ans = []
        for word in B:
            if s[:len(word)] = word:
                if (len(s) == len(word)):
                    ans.append(word)
                else:
                    suffix = s[len(word):]
                    temp = solve(suffix)
                    for t in temp:
                        res.append(word+''+t)
        d[s] =sorted(list(set(ans)))
        return d[s]
    return solve(A)