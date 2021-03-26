# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        nodes = set()
        while A:
            if A in nodes:
                return A
            else:
                nodes.add(A)
            A = A.next
        return None
            
