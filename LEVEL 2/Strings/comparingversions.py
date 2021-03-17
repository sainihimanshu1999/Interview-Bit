class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        version_a = list(map(int , A.split('.')))
        version_b = list(map(int , B.split('.')))
        
        for i in range(max(len(version_a),len(version_b))):
            anum = version_a[i] if i < len(version_a) else 0
            bnum = version_b[i] if i < len(version_b) else 0
            
            if anum<bnum:
                return -1
            elif anum>bnum:
                return 1
        return 0
            
