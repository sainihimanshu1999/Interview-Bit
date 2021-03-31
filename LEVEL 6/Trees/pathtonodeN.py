class Solution:
    def pathtonode(selff,A,B):
        res = []
        def xoxo(root,st,x):
            if not root:
                return None
            if root.val == B:
                st.append(root.val)

                for i in st:
                    res.append(i)

            root.left = xoxo(root.left,st+[A.val],B)
            root.right = xoxo(root.right,st+[A.val],B)
        xoxo(A,[],b)
        return res