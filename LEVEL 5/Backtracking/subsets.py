'''
Basic iterative solution
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        if len(A)==0:
            return [[]]
        A.sort()
        x =[[]]
        for i in range(len(A)):
            for j in range(len(x)):
                x.append(x[j]+[A[i]])
        x.sort()
        i=1
        
        while i<len(x):

            if x[i]==x[i-1]:
                del x[i]
            else:
                i+=1
            
        
        return x
    
        
'''
Back Tracking solution
'''    
res = []
def backtrack(A,subset,index):

   temp = list(subset)
   res.append(temp)
   for i in range(index,len(A)):
       if i>index and A[i]==A[i-1]:
           continue
       else:
           subset.append(A[i])
           backtrack(A,subset,i+1)
           subset.pop()
   return

class Solution:
   # @param A : list of integers
   # @return a list of list of integers
   def subsetsWithDup(self, A):
       global res
       res = []
       A.sort()
       backtrack(A,[],0)
       return res