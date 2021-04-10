class solution:
    def stepnum(self,A,B):
        def checkRange(A,B,val):
            if A<=val<=B:
                return 'in'
            elif val>B:
                return 'out'
            return
        ans = []
        if A == 0:
            ans.append(0)

        queue = [1,2,3,4,5,6,7,8,9]
        while queue:
            curr = queue.pop(0)
            val = checkRange(A,B,curr)
            if val =='in':
                ans.append(curr)
            elif val == 'out':
                break

            if curr%10 != 0:
                queue.append(curr*10+(curr%10)-1)
            if curr%10 != 9:
                queue.append(curr*10+(curr%10)+1)
        return ans


    
    