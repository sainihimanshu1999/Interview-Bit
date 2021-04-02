def solve(self, A):
    arr = []
    arr.append([A,0])
    arr_index = 0
    prev = -1
    ans = []

    while arr_index<len(arr):
        root,level = arr[arr_index]
        if root.right:
            arr.append([root.right,level+1])
        if root.left:
            arr.append([root.left,level+1])
        if prev!=level:
            ans.append(root.val)
        arr_index+=1
        prev = level
    return ans