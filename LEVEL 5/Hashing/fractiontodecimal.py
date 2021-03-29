class Solution:
    def fractiontoDecimal(self, A,B):
        if A == 0:
            return '0'
        sign = -1 if (A<0) ^ (B<0) else 1

        A = abs(A)
        B = abs(B)

        initial = A//B

        res = ''

        if (sign==-1):
            res += '-'

        res += str(initial)

        if(A%B==0):
            return res
        
        res += '.'

        rem = A%B
        mp = {}

        index= 0
        repeating =  False

        while(rem>0 and not repeating):
            if rem in mp:
                index = mp[rem]
                repeating = True
                break
            else:
                mp[rem] = len(res)

            rem = rem*10

            temp = rem//B
            res += str(temp)
            rem = rem%B

        if repeating:
            res+= ')'
            x = res[:index]
            x += '('
            x+= res[index:]
            res = x

        return res