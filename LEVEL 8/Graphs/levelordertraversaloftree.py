def BFS(self,A):
    ans = []
    stack = []
    stack.append(A)

    while stack:
        size = len(stack)
        temp = []
        for i in range(size):
            curr_node = stack[0]
            temp.append(curr_node.val)
            stack.pop(0)
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
        ans.append(list(temp))

    return ans
