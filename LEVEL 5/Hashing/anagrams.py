from collections import defaultdict
class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        groups = defaultdict(list)
        for i in range(len(A)):
            groups[tuple(sorted(A[i]))].append(i+1)
        return list(groups.values())
