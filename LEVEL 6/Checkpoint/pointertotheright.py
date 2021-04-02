class Soution:
    def pointertotheright(self,A):
        A.next = None
        node = A
        while node.left:
            leftmost = node
            while node:
                node.left.next = node.right
                node.right = node.next.left if node.next else None
                node = node.next
            node = leftmost.left
        return A