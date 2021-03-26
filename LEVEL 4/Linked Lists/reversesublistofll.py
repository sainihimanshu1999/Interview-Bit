# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
   def reverseBetween(self, A, B, C):
        main = A
        l=0
        before = None
        head = None
        ref = None
        while A:
            temp = A.next
            l+=1
            if l == B-1:
                before = A
            if l == B:
                head = A
                ref = A
            if l>B and l<=C:
                ref.next = A.next
                A.next = head
                head = A
            A = temp
        if before == None:
            return head
        else:
            before.next = head
            return main
            
            
