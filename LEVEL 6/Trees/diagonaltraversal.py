'''
1st way to do this problem
'''
class Solution:
    from collections import deque
    def solve(self,A):
        if not A:
            return []
        q = deque()
        res = []
        curr = A
        while True:
            if curr:
                res.append(curr.val)
                q.append(curr)
                curr = curr.right
            elif q:
                curr = curr.popleft()
                curr = curr.left
            else:
                break
        return res


'''
2nd way to do this problem
'''

class Solution:
    from collections import deque
    def solve(self,A):
        if not A:
            return []
        q = deque([A])
        ans = []
        while(len(q)):
            node = q.popleft()
            while node:
                ans.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                node =node.right
        return ans
