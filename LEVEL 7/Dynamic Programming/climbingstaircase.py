'''
It is just like fibonacci sequence
'''
class Solution:
    def solve(self,A):
        dp = [0]*(A+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2,A+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[A]