# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        dummy = ListNode(0)
        tail = dummy
        
        while True:
            if A is None:
                tail.next = B
                break
            if B is None:
                tail.next = A
                break
            
            if A.val<=B.val:
                tail.next=A
                A = A.next
            else:
                tail.next = B
                B = B.next
            
            tail = tail.next
        return dummy.next


'''
Recurrsion solution for merging two lists
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        temp = None
        if A is None:
            return B
        if B is None:
            return A
        
        if A.val<=B.val:
            temp = A
            temp.next = self.mergeTwoLists(A.next,B)
        if B.val<=A.val:
            temp = B
            temp.next = self.mergeTwoLists(A,B.next)
            
        return temp