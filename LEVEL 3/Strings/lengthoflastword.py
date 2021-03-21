class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        x = A.strip().split(' ')
        return len(x[-1])