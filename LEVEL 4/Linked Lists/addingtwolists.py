# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        temp1 = A
        temp2 = B
        carry = 0
        curr=new=ListNode(0)
        
        while temp1 or temp2 or carry:
            if temp1:
                carry += temp1.val
                temp1 = temp1.next
            if temp2:
                carry += temp2.val
                temp2=  temp2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry = carry//10
        return new.next
