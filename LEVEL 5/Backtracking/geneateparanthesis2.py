class Solution:
    # @param A : integer
    # @return a list of strings
    def solve(self, n, open_, s):
        if len(s) == 2*n:
            self.ans.append(s)
            return
        if open_ != n:
            self.solve(n, open_ + 1, s + '(')
        if len(s) < 2 * open_:
            self.solve(n, open_, s + ')')
            
    def generateParenthesis(self, A):
        self.ans = []
        self.solve(A, 0, '')
        return self.ans