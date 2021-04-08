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
            if s[:len(word)] == word:
                if (len(s) == len(word)):
                    ans.append(word)
                else:
                    suffix = s[len(word):]
                    temp = solve(suffix)
                    for t in temp:
                        ans.append(word+''+t)
        d[s] =sorted(list(set(ans)))
        return d[s]
    return solve(A)

'''
simple recursive approach
'''

def wordBreak(self,A,B):
    if A == '':
        return [[]]

    ans = []
    for word in B:
        if A[:word] == word:
            if len(A) == len(word):
                ans.append(word)
            else:
                suffix = A[word:]
                temp = self.wordBreak(suffix,B)
                for t in temp:
                    ans.append(word + ' '+temp)
    ans = sorted(list(set(ans)))
    return ans