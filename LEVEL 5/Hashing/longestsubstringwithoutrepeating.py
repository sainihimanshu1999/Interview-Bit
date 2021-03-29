class Solution:
    def lengthofLongestSubstring(self,A):
        start = 0
        max_len = 0 
        mp = {}
        for i, char in enumerate(A):
            if char in mp and mp[char]>=start:
                max_len = max(max_len,i-start)
                start = mp[char]+1
            mp[char]=i  
        return max(max_len,i-start+1)