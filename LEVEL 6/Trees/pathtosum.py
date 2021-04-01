def pathtosum(self,A,B):
    ans = []
    def solve(arr,sm,root):
        if not root:
            return None
        if not root.left and not root.right:
            if root.val+sm  == B:
                ans.append(arr+[root.val])
        else:
            return None
        solve(arr+[root.val],sm+root.val,root.left)
        solve(arr+[root.va], sm+root.val,root.right)
    solve([],0,A)
    return ans