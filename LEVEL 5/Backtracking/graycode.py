def grayCode(self,A):
if(A==1):
return [0,1]
else:
ans = self.grayCode(A-1)
return ans + [x+2**(A-1) for x in ans[::-1]]