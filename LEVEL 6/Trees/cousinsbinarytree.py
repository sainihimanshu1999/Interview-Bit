from collections to deque
class Solution:
    def CousinBinaryTree(self,A):
        found,queue = False,deque[A[0]]

        while queue and not found:
            m = len(queue)
            for _ in range(m):
                node = queue.popleft()
                if node.left and node.left.val == B or node.right and node.right.val == B:
                    found = True
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return [node.val for node in queue]
