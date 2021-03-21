class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        dic = {
            'I':1,
            'IV':4,
            'V':5,
            'VI':6,
            'VII':7,
            'VIII':8,
            'IX':9,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        ref = ['I','IV','V','VI','VIII','IX','X']
        
        num = 0
        prev = 0
        
        for i in range(0,len(A)):
            if A[i:] in ref:
                return num+dic[A[i:]]
            else:
                if dic[A[i]]<=dic[A[prev]]:
                    num += dic[A[i]]
                else:
                    num += dic[A[i]] - (2*dic[A[prev]])
            prev = i
        return num        
