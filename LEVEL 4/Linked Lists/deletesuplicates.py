# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        temp = A
        if temp is None:
            return 
        while temp.next is not None:
            if temp.val == temp.next.val:
                new = temp.next.next
                temp.next = None
                temp.next=new
            else:
                temp = temp.next
        return A
