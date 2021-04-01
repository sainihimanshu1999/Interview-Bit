class Solution:
    def lca(sefl,A,B,C):
        ans = []
        def solve(t):
            if not t:
                return False,False

            la,lb = solve(t.left)
            ra,rb = solve(t.right)

            res = (t.val == B or la or ra , t.val == C or lb or rb)
            if res[0] and res[1]:
                ans.append(n.val)
            return res
        solve(A)
        return ans[0] if ans else -1