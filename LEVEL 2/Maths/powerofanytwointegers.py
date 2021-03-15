class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        B = 2
        while A >= B**2:
            P = 2
            while A >= B ** P:
                if A == B ** P:
                    return 1
                P += 1
            B += 1
        return 0
